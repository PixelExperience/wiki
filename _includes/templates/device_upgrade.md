{% assign device = site.data.devices[page.device] %}

{% include alerts/important.html content="Please read through the instructions at least once completely before actually following them to avoid any problems because you missed something!" %}

## Manually upgrading PixelExperience

{% include alerts/warning.html content="You must do a factory reset before upgrading, so consider backing up your internal storage." %}

{%- unless device.is_ab_device %}
{%- capture recovery_update %}In some cases, a newer PixelExperience version may not install due to an outdated recovery.
Follow your [device's installation guide]({{ "devices/" | append: device.codename | append: "/install" | relative_url }}) to see how you can update your recovery image.{% endcapture %}
{% include alerts/tip.html content=recovery_update %}
{%- endunless %}

The updater app does not support upgrades from one version of PixelExperience to another, and will block installation to any update for a different version. Upgrading manually requires similar steps to installing PixelExperience for the first time.

1. Download the [PixelExperience install package](https://download.pixelexperience.org/{{ device.codename }}) that you'd like to install or [build]({{ "devices/" | append: device.codename | append: "/build" | relative_url }}) the package yourself.
2. Make sure your computer has working `adb`. Setup instructions can be found [here]({{ "help/adb-fastboot-guide/" | relative_url }}).
3. Enable [USB debugging]({{ "help/adb-fastboot-guide/#setting-up-adb" | relative_url }}) on your device.
4. Reboot into recovery by running `adb reboot recovery`, or by performing the following:
    * {{ device.recovery_boot }}
{%- if device.uses_custom_recovery %}
5. Now tap **Wipe**.
6. Now tap **Format Data** and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage.
7. Sideload the PixelExperience `.zip` package:
    * On the device, select "Advanced", "ADB Sideload", then swipe to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/tip.html content="If the process succeeds the output will stop at 47% and report `adb: failed to read command: Success/No error`." %}
{% else %}
5. Now tap **Factory Reset**, then **Format data / factory reset** and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage, as well as format your cache partition (if you have one).
6. Return to the main menu.
7. Sideload the PixelExperience `.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/tip.html content="If the process succeeds the output will stop at 47% and report `adb: failed to read command: Success/No error`." %}
{% endif %}
{% if device.uses_custom_recovery %}
8. Once you have installed everything successfully, run 'adb reboot'.
{% else %}
8. Once you have installed everything successfully, click the back arrow in the top left of the screen, then "Reboot system now".
{% endif %}

{% include alerts/specific/warning_recovery_app.html %}
{% include alerts/specific/tip_sideload_stuck_47.html %}

## Get assistance

If you have any questions or get stuck on any of the steps, feel free to ask on [our Telegram group](https://t.me/pixelexperiencechat).
