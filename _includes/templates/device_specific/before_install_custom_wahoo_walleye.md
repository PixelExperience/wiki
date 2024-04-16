## Pre-install instructions
Starting with Android 12, you must re-partition the device for PixelExperience to be installed.

{% include alerts/warning.html content="Your data will be lost, please do a backup." %}

If you want to revert to the stock partition table, kindly flash the official Google factory image:<br />
[Pixel 2 Official Factory Image](https://developers.google.com/android/images#walleye)

1. Download the following zip for your version:
    * [Product Partiton Extended - Pixel 2](https://wiki-blobs-dl.pixelexperience.org/wiki_blobs_wahoo/main/productpartition-pixel2-extended.zip)
        * PixelExperience 13 and above
    * [Product Partition - Pixel 2](https://wiki-blobs-dl.pixelexperience.org/wiki_blobs_wahoo/main/productpartition-pixel2.zip)
        * PixelExperience 12
2. If you are not in recovery, reboot into recovery:
    * {{ device.recovery_boot }}
3. Sideload the `.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/tip.html content="If the process succeeds the output will stop at 47% and report `adb: failed to read command: Success/No error`." %}
4. Return to the main menu.
5. Now tap **Factory Reset**, then **Format data / factory reset** and continue with the formatting process.
