{%- assign device = site.data.devices[page.device] -%}
{% if device.custom_recovery_link %}
{% assign custom_recovery_link = device.custom_recovery_link %}
{% else %}
{% assign custom_recovery_link = "https://dl.twrp.me/" | append: device.codename %}
{% endif %}

## Installing a custom recovery using `edl`


{% if device.uses_custom_recovery %}
1. Download the [custom recovery]({{ custom_recovery_link }}).
{% else %}
1. Download the [PixelExperience Recovery](https://download.pixelexperience.org/{{ device.codename }}). Simply download the latest recovery file.
{% endif %}
2. Connect your device to your PC via USB.
3. On the computer, open a command prompt (on Windows) or terminal (on Linux or macOS) window, and type:
```
adb reboot edl
```
    {% if device.edl_boot %}
    You can also boot into edl mode via a key combination:

    * {{ device.edl_boot }}
    {% endif %}
4. Flash recovery into your device by following [this]({{ device.install_recovery_guide }}) guide.
