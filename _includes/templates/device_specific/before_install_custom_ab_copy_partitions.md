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
