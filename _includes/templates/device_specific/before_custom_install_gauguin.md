## Pre-install instructions
Starting with PixelExperience, you must install the stable Android 11 MIUI first for PixelExperience to be installed.

{% include alerts/note.html content="If you have installed the stable Android 11 MIUI or you have installed the stable Android 11 MIUI vendor, you won't need to flash again." %}

1. Download the correct stable Android 11 MIUI according to the version of your phone:
    * [Redmi Note 9 Pro 5G](https://bigota.d.miui.com/V12.0.2.0.RJSCNXM/miui_GAUGUIN_V12.0.2.0.RJSCNXM_648ec563d6_11.0.zip)
    * [Xiaomi Mi 10i](https://bigota.d.miui.com/V12.0.1.0.RJSINXM/miui_GAUGUININGlobal_V12.0.1.0.RJSINXM_eb9e93c32b_11.0.zip)
    * [Xiaomi Mi 10T Lite(Global)](https://bigota.d.miui.com/V12.0.2.0.RJSMIXM/miui_GAUGUINGlobal_V12.0.2.0.RJSMIXM_5eb45c65a7_11.0.zip)
    * [Xiaomi Mi 10T Lite(Taiwan)](https://bigota.d.miui.com/V12.0.2.0.RJSMIXM/miui_GAUGUINGlobal_V12.0.2.0.RJSMIXM_5eb45c65a7_11.0.zip)
    * [Xiaomi Mi 10T Lite(EEA)](https://bigota.d.miui.com/V12.0.1.0.RJSEUXM/miui_GAUGUINEEAGlobal_V12.0.1.0.RJSEUXM_15bfbef742_11.0.zip)
2. If you are not in recovery, reboot into recovery: 
    * With the device powered off, hold `Volume Up` + `Power`. Keep holding both buttons until the “MI” logo appears on the screen, then release.
3. Sideload the `.zip` package:
    * On the device, select “Apply Update”, then “Apply from ADB” to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/tip.html content="If the process succeeds the output will stop at 47% and report `adb: failed to read command: Success/No error`." %}
4. Return to the main menu.
5. Now tap Factory Reset, then Format data / factory reset and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage, as well as format your cache partition (if you have one).
