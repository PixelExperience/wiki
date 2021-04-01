{% assign device = site.data.devices[page.device] %}

{% include alerts/important.html content="Please read through the instructions at least once completely before actually following them to avoid any problems because you missed something!" %}

{% capture upgrade_only %}These instructions only apply to version upgrades. If you wish to downgrade to an earlier version of PixelExperience, follow your [device's]({{ "devices/" | append: device.codename | append: "/install" | relative_url }}) instructions for installing PixelExperience the first time.{% endcapture %}

{% include alerts/warning.html content="We recomend a factory reset before upgrading." %}
{% include alerts/warning.html content=upgrade_only %}

## Manually upgrading PixelExperience

{%- unless device.is_ab_device %}
{%- capture recovery_update %}In some cases, a newer PixelExperience version may not install due to an outdated recovery.
Follow your [device's installation guide]({{ "devices/" | append: device.codename | append: "/install" | relative_url }}) to see how you can update your recovery image.{% endcapture %}
{% include alerts/tip.html content=recovery_update %}
{%- endunless %}

The updater app does not support upgrades from one version of PixelExperience to another, and will block installation to any update for a different version. Upgrading manually requires similar steps to installing PixelExperience for the first time.

1. Download the [PixelExperience install package](https://download.pixelexperience.org/{{ device.codename }}) that you'd like to install or [build]({{ "devices/" | append: device.codename | append: "/build" | relative_url }}) the package yourself.
2. Make sure your computer has working `adb`. Setup instructions can be found [here]({{ "help/adb-fastboot-guide/" | relative_url }}).
3. Enable [USB debugging]({{ "help/adb-fastboot-guide/#setting-up-adb" | relative_url }}) on your device.
{%- if device.format_on_upgrade %}
4. Reboot into recovery by running `adb reboot recovery`, or by performing the following:
    * {{ device.recovery_boot }}
5. Wipe your data partition (this is usually named "Wipe", or "Format")
    {% include alerts/warning.html content="Without this step your device will not boot on the new version!" %}
{%- if device.uses_twrp != true %}
6. Click `Advanced`, then `Enable ADB`.
{%- endif %}
{%- endif %}
4. Run `adb reboot sideload`.
    {% include alerts/important.html content="The device may reboot to a blank black screen, fear not, this is a known bug on some recoveries, proceed with the instructions." %}
5. Run `adb sideload /path/to/zip` (inserting the path to your PixelExperience package).
{% if device.is_ab_device and device.uses_custom_recovery %}
6. _(Optionally)_: If you want to install any additional add-ons, run `adb reboot sideload` once more, then `adb sideload /path/to/zip` those packages in sequence.
{% elsif device.is_ab_device %}
6. _(Optionally)_: If you want to install any additional add-ons, click `Advanced`, then `Reboot to Recovery`, then when your device reboots, click `Apply Update`, then `Apply from ADB`, then `adb sideload /path/to/zip` those packages in sequence.
{% elsif device.uses_custom_recovery %}
6. _(Optionally)_: If you want to install any additional add-ons, click `Advanced`, then `ADB Sideload`, then swipe to begin sideload, then `adb sideload /path/to/zip` those packages in sequence.
{% else %}
6. _(Optionally)_: If you want to install any additional add-ons, click `Apply Update`, then `Apply from ADB`, then `adb sideload /path/to/zip` those packages in sequence.
{% endif %}

{% if device.uses_custom_recovery and device.is_ab_device != true %}
7. Once you have installed everything successfully, run `adb reboot`.
{% else %}
7. Once you have installed everything successfully, click the back arrow in the top left of the screen, then "Reboot system now".
{% endif %}

{% include alerts/specific/warning_recovery_app.html %}
{% include alerts/specific/tip_sideload_stuck_47.html %}

## Get assistance

If you have any questions or get stuck on any of the steps, feel free to ask on [our Telegram group](https://t.me/pixelexperiencechat).
