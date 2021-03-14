## Pre-install instructions
Starting with Android 11, you must re-partition the device for PixelExperience to be installed.

{% include alerts/warning.html content="Your data will be lost, please do a backup." %}

{% include alerts/note.html content="If you install the stock rom again, you must repeat the procedure." %}

1. Download the correct zip according to the version of your phone:
    * [Pixel/Pixel XL (32GB)](https://github.com/PixelExperience-Devices/blobs/raw/main/repartition-ogpixel-32gb.zip)
    * [Pixel/Pixel XL (128GB)](https://github.com/PixelExperience-Devices/blobs/raw/main/repartition-ogpixel-128gb.zip)
2. Sideload the `.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/tip.html content="If the process succeeds the output will stop at 47% and report `adb: failed to read command: Success/No error`." %}
3. Return to the main menu.
4. Now tap **Factory Reset**, then **Format data / factory reset** and continue with the formatting process.
