{%- assign device = site.data.devices[page.device] %}
{%- assign path_prefix = "devices/" | append: device.codename %}

{% include alerts/important.html content="Please read through the instructions at least once completely before actually following them to avoid any problems because you missed something!" %}

{%- if device.before_install and device.before_install == "needs_specific_android_fw" %}
{% unless device.before_install_args and device.before_install_args.ships_fw %}
{% capture path %}templates/device_specific/before_install_{{ device.before_install }}.md{% endcapture %}
{% include {{ path }} %}
{% endunless %}
{%- endif %}

## Manually upgrading PixelExperience

{%- unless device.format_on_upgrade %}
{% include alerts/note.html content="Following these instructions will **not** wipe your data. It is, however, recommended to save important data before doing so, anyway!" %}
{%- endunless %}

{% include alerts/warning.html content="You must do a factory reset before upgrading, so consider backing up your internal storage." %}

{%- unless device.is_ab_device %}
{%- capture recovery_update %}In some cases, a newer PixelExperience version may not install due to an outdated recovery.
Follow your [device's installation guide]({{ path_prefix | append: "/install" | relative_url }}) to see how you can update your recovery image.{% endcapture %}
{% include alerts/tip.html content=recovery_update %}
{%- endunless %}

The updater app does not support upgrades from one version of PixelExperience to another, and will block installation to any update for a different version. Upgrading manually requires similar steps to installing PixelExperience for the first time.

1. Download the [PixelExperience install package](https://download.pixelexperience.org/{{ device.codename }}) that you'd like to install or [build]({{ path_prefix | append: "/build" | relative_url }}) the package yourself.
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
        {% include alerts/specific/tip_adb_flash_success.html %}
{% else %}
5. Now tap **Factory Reset**, then **Format data / factory reset** and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage, as well as format your cache partition (if you have one).
6. Return to the main menu.
7. Sideload the PixelExperience `.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/specific/tip_adb_flash_success.html %}
{% endif %}
{% if device.uses_custom_recovery %}
8. Once you have installed everything successfully, run 'adb reboot'.
{% else %}
8. Once you have installed everything successfully, click the back arrow in the top left of the screen, then "Reboot system now".
{% endif %}

{%- if device.custom_recovery_link or device.uses_twrp %}
{% include alerts/specific/warning_recovery_app.html %}
{%- endif %}
{% include alerts/specific/tip_sideload_stuck_47.html %}

## Get assistance

If you have any questions or get stuck on any of the steps, feel free to ask on [our Telegram group](https://t.me/pixelexperiencechat).
