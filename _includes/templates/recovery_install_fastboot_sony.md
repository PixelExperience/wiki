{%- assign device = site.data.devices[page.device] -%}
{% if device.custom_recovery_link %}
{% assign custom_recovery_link = device.custom_recovery_link %}
{% else %}
{% assign custom_recovery_link = "https://dl.twrp.me/" | append: device.codename %}
{% endif %}

## Unlocking the bootloader

{% include alerts/note.html content="The steps below only need to be run once per device." %}
{% include alerts/warning.html content="Unlocking the bootloader will erase all data on your device!
This also includes your DRM keys, which are stored in the Trim Area partition (also called TA).
Before proceeding, ensure the data you would like to retain is backed up to your PC and/or your Google account, or equivalent. Please note that OEM backup solutions like Samsung and Motorola backup may not be accessible from PixelExperience once installed.
If you wish to backup the TA partition first, you can find tutorials related to your device on the internet." %}

{% if device.install_variant and device.install_variant contains "sony_unlock_contacts" %}
1. Open the `Contacts` app.
2. Click on the menu button in the top right.
3. Click on `Settings`.
4. Long press (for about 5 seconds) somewhere in the empty space just above navigation bar, then release your finger. A button named `Enter service code` will then appear in the same area (this may take a few attempts).
5. Click on `Enter service code`. A dialer will appear.
{% endif %}

1. On the device, dial `*#*#7378423#*#*` (`*#*#SERVICE#*#*`) to launch the service menu.
2. Go to `service info` > `configuration` and check `rooting status` - you can only continue if it says `Bootloader unlock allowed: Yes`.
3. Connect the device to your PC via USB.
4. On the computer, open a command prompt (on Windows) or terminal (on Linux or macOS) window, and type:
```
adb reboot bootloader
```
    {% if device.download_boot %}
    You can also boot into fastboot mode via a key combination:

    * {{ device.download_boot }}
    {% endif %}
5. Once the device is in fastboot mode, verify your PC finds it by typing:
```
fastboot devices
```
    {% include alerts/tip.html content="If you see `no permissions fastboot` while on Linux or macOS, try running `fastboot` as root." %}
6. Follow the instructions on [Sony's official unlocking website](http://developer.sonymobile.com/unlockbootloader/unlock-yourboot-loader/) to generate an unlock code for your bootloader.
7. Use your code to unlock the bootloader of your device:
```
fastboot oem unlock <your_unlock_code>
```
8. Since the device resets completely, you will need to re-enable USB debugging to continue.

{% if device.install_variant and device.install_variant contains "sony_init_fota" %}


## Installing a custom recovery using `fastboot`

{% if device.uses_custom_recovery %}
1. Download the [custom recovery]({{ custom_recovery_link }}).
{% else %}
1. Download the [PixelExperience Recovery](https://download.pixelexperience.org/{{ device.codename }}). Simply download the latest recovery file.
{% endif %}
2. Connect your device to your PC via USB.
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
    {% include alerts/tip.html content="If you see `no permissions fastboot` while on Linux or macOS, try running `fastboot` as root." %}
{% if device.has_recovery_partition %}
5. Flash the custom recovery to `recovery` partition:
```
fastboot flash recovery path-to-recovery-file.img
```
{% else %}
5. Temporarily flash the custom recovery to `boot`:
```
fastboot flash boot path-to-recovery-file.img
```
{% endif %}
    {% include alerts/tip.html content="The file may not be named identically to what stands in this command, so adjust accordingly. Remember to adjust the filename in the following commands as well." %}
6. Reboot to the custom recovery:
```
fastboot reboot
```
7. Push the custom recovery image to your device:
```
adb push path-to-recovery-file.img /sdcard
```
8. Enter shell on the device:
```
adb shell
```
9. Flash custom recovery to `recovery` permanently:
```
dd if=/sdcard/path-to-recovery-file.img of=/dev/block/platform/msm_sdcc.1/by-name/FOTAKernel
```
10. Exit the adb shell:
```
exit
```
{% else %}

{% if device.is_ab_device %}
{% include templates/recovery_install_fastboot_ab.md %}
{% else %}
{% include templates/recovery_install_fastboot_generic.md %}
{% endif %}

{% endif %}
