{% assign device = site.data.devices[page.device] %}

## Using the PixelExperience Updater app

1. Open Settings, navigate to "System", tap on "Advanced" and tap on "System update".
2. Click the Refresh Icon in the top right corner.
3. If an update is available, press the "Download" button.
{%- if device.is_ab_device %}
4. When the download completes, click "Install". Once the update process has finished, the device will display a "Reboot" button, you may need to go into the Updater menu in Settings, "System" to see it. This will reboot you into the updated system.
{%- else %}
4. When the download completes, click "Install". Your device will reboot to recovery and install the update, then reboot to the updated installation.
{%- endif %}

{% unless device.is_ab_device%}
## Sideloading from Recovery
1. Make sure your computer has working `adb`. Setup instructions can be found [here]({{ "help/adb-fastboot-guide/" | relative_url }}).
2. Enable [USB debugging]({{ "help/adb-fastboot-guide/#setting-up-adb" | relative_url }}) on your device.
5. Run: `adb reboot sideload`
6. Run: `adb sideload /path/to/zip`
{% if device.uses_twrp %}
7. Run: `adb reboot`
{% else %}
7. Click the back arrow in the top left of the screen, then "Reboot system now".
{% endif %}
{% endunless %}
