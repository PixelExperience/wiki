{%- assign device = site.data.devices[page.device] -%}
{% if device.custom_recovery_codename %}
{% assign custom_recovery_codename = device.custom_recovery_codename %}
{% else %}
{% assign custom_recovery_codename = device.codename %}
{% endif %}

## Installing a custom recovery using `edl`


{% if device.uses_twrp %}
{% if device.custom_twrp_link %}
1. Download a custom recovery - you can download [TWRP]({{ device.custom_twrp_link }}). Simply download the latest recovery file, named something like `twrp-x.x.x-x-{{ custom_recovery_codename }}.img`.
{% else %}
1. Download a custom recovery - you can download [TWRP](https://dl.twrp.me/{{ custom_recovery_codename }}). Simply download the latest recovery file, named something like `twrp-x.x.x-x-{{ custom_recovery_codename }}.img`.
{% endif %}
{% else %}
1. Download a custom recovery - you can download [PixelExperience Recovery](https://download.pixelexperience.org/{{ custom_recovery_codename }}). Simply download the latest recovery file.
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
