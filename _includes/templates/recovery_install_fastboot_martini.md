{%- assign device = site.data.devices[page.device] -%}

## Unlocking the bootloader

{% include alerts/note.html content="The steps below only need to be run once per device." %}
{% include alerts/warning.html content="Unlocking the bootloader will erase all data on your device!
Before proceeding, ensure the data you would like to retain is backed up to your PC and/or your Google account, or equivalent. Please note that OEM backup solutions like Samsung and Motorola backup may not be accessible from PixelExperience once installed." %}

{% unless device.no_oem_unlock_switch %}
1. Enable OEM unlock in the Developer options under device Settings, if present.
{% endunless %}
2. Connect the device to your PC via USB.
3. On the computer, open a command prompt (on Windows) or terminal (on Linux or macOS) window, and type:
```
adb reboot bootloader
```
    {% if device.download_boot %}
    You can also boot into fastboot mode via a key combination:

    * {{ device.download_boot }}
    {% endif %}
4. Once the device is in fastboot mode, verify your PC finds it by typing:
```
fastboot devices
```
  If you don't get any output or an error:
   * on Windows: make sure the device appears in the device manager without a triangle. Try other drivers until the command above works!
   * on Linux or macOS: If you see `no permissions fastboot` try running `fastboot` as root. When the output is empty, check your USB cable and port!
5. Now type the following command to unlock the bootloader:

{% if device.custom_unlock_cmd %}
    ```
{{ device.custom_unlock_cmd }}
    ```
{% else %}
    ```
fastboot flashing unlock
    ```
{% endif %}
    {% include alerts/note.html content="At this point the device may display on-screen prompts which will require interaction to continue the process of unlocking the bootloader. Please take whatever actions the device asks you to to proceed." %}
6. If the device doesn't automatically reboot, reboot it. It should now be unlocked.
7. Since the device resets completely, you will need to re-enable USB debugging to continue.

## Before Flashing Rom

{% include alerts/warning.html content="This device needs `boot` `vendor_boot` and `dtbo` from stock rom before flashing the rom,so the process to do so is described below." %}

1. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_martini/-/raw/main/android-13/boot.img?inline=false) `boot.img` file.
2. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_martini/-/raw/main/android-13/vendor_boot.img?inline=false) `vendor_boot.img` file.
3. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_martini/-/raw/main/android-13/dtbo.img?inline=false) `dtbo.img` file.
4. Power off the device, and boot it into bootloader mode:
    * {{ device.download_boot }}
5. Flash a the downloaded images to your device by typing:
```
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash dtbo dtbo.img
```
