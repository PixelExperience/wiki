## Pre-install instructions
Starting with PixelExperience, you must install the stable Android 11 MIUI first for PixelExperience to be installed.

{% include alerts/note.html content="If you have installed the stable Android 11 MIUI or you have installed the stable Android 11 MIUI vendor, you won't need to flash again." %}

1. Download the correct stable Android 11 MIUI according to the version of your phone:
    * [Redmi K30 5G](https://bigota.d.miui.com/V12.5.2.0.RGICNXM/miui_PICASSO_V12.5.2.0.RGICNXM_8f5c35ebbc_11.0.zip)
    * [Redmi K30i](https://bigota.d.miui.com/V12.5.2.0.RGICMXM/miui_PICASSO48M_V12.5.2.0.RGICMXM_4df2ef51db_11.0.zip)
2. If you are not in recovery, reboot into recovery: 
    * With the device powered off, hold `Volume Up` + `Power`. Keep holding both buttons until the “MI” logo appears on the screen, then release.
3. Sideload the `.zip` package:
    * On the device, select “Advanced”, “ADB Sideload”, then swipe to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/tip.html content="If the process succeeds the output will stop at 47% and report `adb: failed to read command: Success/No error`." %}
4. Return to the main menu.
5. Now tap Wipe.
6. Now tap Format Data and continue with the formatting process. 
    This will remove encryption and delete all files stored in the internal storage. 