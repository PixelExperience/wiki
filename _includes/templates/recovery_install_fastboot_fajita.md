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
```
fastboot oem unlock
```

    {% include alerts/note.html content="At this point the device may display on-screen prompts which will require interaction to continue the process of unlocking the bootloader. Please take whatever actions the device asks you to to proceed." %}
6. If the device doesn't automatically reboot, reboot it. It should now be unlocked.
7. Since the device resets completely, you will need to re-enable USB debugging to continue.

## Before Flashing Rom

## Ensuring all firmware partitions are consistent

{% include alerts/note.html content="The steps below only need to be run once per device." %}

In some cases, the inactive slot can be unpopulated or contain much older firmware than the active slot, leading to various issues including a potential hard-brick. We can ensure none of that will happen by copying the contents of the active slot to the inactive slot.

To do this, sideload the copy-partitions-20210323_1922.zip package by doing the following:
1. Download the `copy-partitions-20210323_1922.zip` file from [here](https://github.com/PixelExperience-Devices/blobs/blob/main/copy-partitions-20210323_1922.zip?raw=true).
{%- if device.uses_custom_recovery %}
2. Sideload the `copy-partitions-20210323_1922.zip` package:
    * On the device, select "Advanced", "ADB Sideload", then swipe to begin sideload
    * On the host machine, sideload the package using: `adb sideload filename.zip`
{%- else %}
2. Sideload the `copy-partitions-20210323_1922.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload copy-partitions-20210323_1922.zip`
3. Now reboot to recovery by tapping "Advanced", then "Reboot to recovery".
{%- endif %}

## Initializing Dynamic partitions
You can acquire more information about dynamic partitions [here](https://source.android.google.cn/docs/core/ota/dynamic_partitions/implement)

{% include alerts/warning.html content="Dynamic partitions must be initialized when installing for the first time, so the process to do so is described below." %}
1. Download [this](https://sourceforge.net/projects/sn-roms/files/PixelExperience-13/fajita/super_empty.img/download) `super_empty.img` file.
2. Power off the device, and boot it into `bootloader` mode
3. Flash vbmeta from [here](https://sourceforge.net/projects/sn-roms/files/PixelExperience-13/fajita/vbmeta.img/download):
```
fastboot flash vbmeta_a vbmeta.img
fastboot flash vbmeta_b vbmeta.img
```
4. Flash PixelExperience Recovery:
```
fastboot flash boot <recovery_filename>.img
```
5. Erase the old android partitions with the following:
```
fastboot erase system_a
fastboot erase system_b
fastboot erase odm_a
fastboot erase odm_b
fastboot erase vendor_a
fastboot erase vendor_b
```
6. Now reboot into `recovery` and enter `fastbootd mode`

7. Initialize the retrofit super partitions for each slot:
```
fastboot wipe-super super_empty.img
fastboot set_active other
fastboot wipe-super super_empty.img
fastboot set_active other
```

8. Choose `Enter recovery` to return to `recovery`
