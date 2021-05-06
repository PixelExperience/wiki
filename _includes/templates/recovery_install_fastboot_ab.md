{%- assign device = site.data.devices[page.device] -%}
{% if device.custom_recovery_link %}
{% assign custom_recovery_link = device.custom_recovery_link %}
{% else %}
{% assign custom_recovery_link = "https://dl.twrp.me/" | append: device.codename %}
{% endif %}

{% if device.has_recovery_partition %}
## Booting a custom recovery using `fastboot`
{% else %}
## Temporarily booting a custom recovery using `fastboot`
{% endif %}

{% if device.uses_custom_recovery %}
1. Download the [custom recovery]({{ custom_recovery_link }}).
{% else %}
1. Download the [PixelExperience Recovery](https://download.pixelexperience.org/{{ device.codename }}). Simply download the latest recovery file.
{% endif %}
2. Connect your device to your PC via USB.
3. On the computer, open a command prompt (on Windows) or terminal (on Linux or macOS) window, and type:
```
adb reboot bootloader
```
    {% if device.download_boot %}
    You can also boot into fastboot mode via a key combination:

    * {{ device.download_boot }}
    {% endif %}
4. Once the device is in fastboot mode, verify your PC finds it by typing:
```
fastboot devices
```
    {% include alerts/tip.html content="If you see `no permissions fastboot` while on Linux or macOS, try running `fastboot` as root." %}
    {% include alerts/tip.html content="Some devices have buggy USB support while in bootloader mode, if you see `fastboot` hanging with no output when using commands such as `fastboot getvar .. `, `fastboot boot ...`, `fastboot flash ...` you may want to try a different USB port (preferably a USB Type-A 2.0 one) or a USB hub." %}
{% if device.has_recovery_partition %}
5. Flash the recovery on your device by typing:
```
fastboot flash recovery <recovery_filename>.img
```
{% else %}
5. Temporarily flash a recovery on your device by typing:
```
fastboot flash boot <recovery_filename>.img
```
    {% include alerts/note.html content="Outdated fastboot releases dropped legacy A/B support, so it might attempt to flash to `boot__a` / `boot__b` rather than `boot_a` / `boot_b` if you try to flash `boot`. In this case, you must update `fastboot` to a release newer than or equal to `31.0.2`. Alternatively, you can manually specify which slot to flash to based on what slot fastboot failed to flash to. For example, if fastboot fails to flash to `boot__a`, you must flash to `boot_a`." %}
    {% include alerts/tip.html content="The file may not be named identically to what stands in this command, so adjust accordingly." %}
{% endif %}

{% unless site.data.devices[page.device].no_fastboot_boot %}
{% if device.uses_custom_recovery %}
    Alternatively, on some devices and recoveries you can use fastboot to boot directly into the freshly flashed or any other desired recovery:
```
fastboot boot <recovery_filename>.img
```
    {% include alerts/tip.html content="The file may not be named identically to what stands in this command, so adjust accordingly." %}
{% endif %}
{% endunless %}
