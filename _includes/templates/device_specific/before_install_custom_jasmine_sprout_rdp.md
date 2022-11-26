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

## Pre-install instructions

For PixelExperience, you must flash the `super_empty.img` to make your device compatible for dynamic retrofit partition.

{% include alerts/note.html content="If you already have flashed super_empty.img and are using another ROM then you don't need to reflash it" %}

{% include alerts/note.html content="These steps needs to be done only once, and for first time installation only" %}

To flash Super_Empty.img head over to [THIS](https://github.com/PixelExperience-Devices/device_xiaomi_jasmine_sprout/releases/download/v1.0.0/super_empty.img) link and download the `super_empty.img`.
1. Boot up PixelExperience recovery
2. Go to "Advanced" -> "Enter fastboot"
   {% include alerts/warning.html content="The \"Enter fastboot\" option may not be present on older PixelExperience recovery builds and it cannot be substituted with \"Reboot to bootloader\"." %}
3. And then in fastbootd [NOT FASTBOOT/BOOTLOADER] `fastboot wipe-super <super_empty>.img` . Now continue to flash the zip file normally
