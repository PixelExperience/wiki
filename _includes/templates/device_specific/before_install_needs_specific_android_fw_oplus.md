{% capture content -%}
Before following these instructions please ensure that the device is currently using **Android {{ device.before_install_args.version }}** firmware.<br/>
If the vendor provided multiple updates for that version, e.g. security updates, make sure you are on the latest!<br/>
If your current installation is newer or older than **Android {{ device.before_install_args.version }}**, please up- or downgrade to the required version before proceeding
{%- if device.firmware_update and page.url contains "upgrade" %}
by following [this guide]({{ "devices/" | append: device.codename | append: "/fw_update" | relative_url }})
{%- else %}
(guides can be found on the internet!).
{%- endif %}
Also note that you cannot directly unlock the bootloader if you are on OxygenOS 12.1. For unlocked bootloader on OxygenOS 12.1, you will need to unlock the bootloader on OxygenOS 11 first and then update to OxygenOS 12.1.
{%- endcapture %}

{% include alerts/warning.html content=content %}
