{%- assign device = site.data.devices[page.device] -%}

## Unlocking the bootloader

{% include alerts/note.html content="The steps below only need to be run once per device." %}
{% include alerts/warning.html content="Unlocking the bootloader will erase all data on your device!
Before proceeding, ensure the data you would like to retain is backed up to your PC and/or your Google account, or equivalent. Please note that OEM backup solutions like Samsung and Motorola backup may not be accessible from PixelExperience once installed." %}

{% unless device.no_oem_unlock_switch %}
1. Enable OEM unlocking and USB debugging in the Developer options under device Settings, if present.
2. Visit [Lenovo's bootloader unlock page](https://www.zui.com/iunlock) in a web browser.
3. Fill out the form with your device's IMEI, serial number, and your email. Complete the captcha and accept the terms that you're voiding your warranty by choosing to unlock your bootloader.
    {% include alerts/tip.html content="You can get the IMEI by typing `*#06#` into the dialer. You can get the serial number by going to About phone -> Technical details -> Status in the Settings app" %}
4. After some time, you should get an email from ```devworld@lenovo.com``` with a link to your unlock token. Download it to your computer.
{% endunless %}
5. Connect the device to your PC via USB.
6. On the computer, open a command prompt (on Windows) or terminal (on Linux or macOS) window, and type:
```
adb reboot bootloader
```
    {% if device.download_boot %}
    You can also boot into fastboot mode via a key combination:

    * {{ device.download_boot }}
    {% endif %}
7. Once the device is in fastboot mode, verify your PC finds it by typing:
```
fastboot devices
```
    {% include alerts/tip.html content="If you see `no permissions fastboot` while on Linux or macOS, try running `fastboot` as root." %}
8. Type the following command to flash the unlock token:
```
fastboot flash unlock sn.img
``` 

9. Now type the following command to unlock the bootloader:

{% if device.custom_unlock_cmd %}
    ```
{{ device.custom_unlock_cmd }}
    ```
{% else %}
    ```
fastboot oem unlock
    ```
{% endif %}

10. The device will automatically reboot, and your bootloader will be unlocked. Since the device resets completely, you will need to re-enable USB debugging to continue.

{% if device.before_recovery_install %}
{% capture path %}templates/device_specific/{{ device.before_recovery_install }}.md{% endcapture %}
{% include {{ path }} %}
{% endif %}

{% include templates/recovery_install_fastboot_generic.md %}
