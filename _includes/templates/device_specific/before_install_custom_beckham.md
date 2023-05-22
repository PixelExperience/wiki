## Ensuring all firmware partitions are consistent

{% include alerts/note.html content="The steps below only need to be run once per device." %}

In some cases, the inactive slot can be unpopulated or contain much older firmware than the active slot, leading to various issues including a potential hard-brick. We can ensure none of that will happen by copying the contents of the active slot to the inactive slot.

To do this, sideload the copy-partitions-20210323_1922.zip package by doing the following:
1. Download the `copy-partitions-20210323_1922.zip` file from [here](https://github.com/PixelExperience-Devices/blobs/blob/main/copy-partitions-20210323_1922.zip?raw=true).
2. Sideload the `copy-partitions-20210323_1922.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload copy-partitions-20210323_1922.zip`
3. Now reboot to recovery by tapping "Advanced", then "Reboot to recovery".

## RETROFIT INSTRUCTIONS:

1- You need Pixel Experience recovery installed (MANDATORY -TWRP WON'T WORK)
If you are on PixelExperience 11 you already must have installed, it works. if not, download from PE website

2-You need to install retrofit zip to convert your device, this step only need to be run once per device.
Download [here](https://mega.nz/file/DAU1hABZ#0CjaYVAYntkIjKN2R_6qtCSKCKvIoPh1lDtXyrl0_gM).

3- Go to PixelExperience recovery and format your data, then sideload or install from sdcard previosly downloaded retrofit.zip. Format your data and reboot to recovery.

4-Download the updated build of PixelExperience from [here](https://get.pixelexperience.org/beckham), sideload or move to your sdcard and install the updated system, format your data and done

FAQ:
1- Can I install magisk in this retrofited system?
yes, you can either sideload by adb or install from sdcard renaming magisk.apk to magisk.zip

2- Why the hell use the retrofited system?
Our system partition is small. Retrofited system allow us to ship all the pixel goodies
reference [here](https://source.android.com/devices/tech/ota/dynamic_partitions).

3- How do I go back to the old schema:
Easy as you converted:
- Pick any rom with a/b schema (eg lineageOS or PE 12)
- Reboot recovery
- Format data
- Flash a/b zip
-Done

DO NOT USE TWRP FOR RETROFITED ROMS, IT WILL BREAK YOUR PARTITIONS
