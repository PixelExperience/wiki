{%- assign device = site.data.devices[page.device] -%}
{% if device.custom_recovery_link %}
{% assign custom_recovery_link = device.custom_recovery_link %}
{% else %}
{% assign custom_recovery_link = "https://dl.twrp.me/" | append: device.codename %}
{% endif %}

## Rooting your device

{% include alerts/important.html content="The device must be rooted before proceeding any further." %}

{% case device.root_method[0] %}
{% when 'custom' %}
1. Root your device by following [this]({{ device.root_method[1] }}) guide.
{% when 'kingroot' %}
1. Download KingRoot from [here](https://kingroot.net/).
   1. Install and run the apk to achieve root. Ensure you have a working Internet connection.
{% when 'towelroot' %}
1. Download TowelRoot from [here](https://towelroot.com/).
   1. Click the large lambda symbol to download the apk.
   2. Install and run the apk to achieve root.
{% endcase %}

{% if device.before_dd_recovery %}
{% capture path %}templates/device_specific/{{ device.before_dd_recovery }}.md{% endcapture %}
{% include {{ path }} %}
{% endif %}

## Installing a custom recovery using `dd`

{% if device.uses_custom_recovery %}
1. Download the [custom recovery]({{ custom_recovery_link }}).
{% else %}
1. Download the [PixelExperience Recovery](https://download.pixelexperience.org/{{ device.codename }}). Simply download the latest recovery file.
{% endif %}
2. Place the recovery image file on the root of `/sdcard`:
   * Using adb: `adb push <recovery_filename>.img /sdcard/<recovery_filename>.img`
    {% include alerts/tip.html content="The file may not be named identically to what stands in this command, so adjust accordingly." %}
   * You can use any method you are comfortable with. `adb` is universal across all devices, and works both in Android and recovery mode, providing USB debugging is enabled.
3. Now, open an `adb shell` from a command prompt (on Windows) or terminal (on Linux or macOS) window. In that shell, type the following commands:
```
su
dd if=/sdcard/<recovery_filename>.img of={{ device.recovery_partition }}
```
4. Reboot into recovery.
    * From the same shell, type the following command:
```
reboot recovery
```
