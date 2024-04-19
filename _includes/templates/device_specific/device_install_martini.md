{% assign device = site.data.devices[page.device] %}
{% include alerts/warning.html content="These instructions only work if you follow every section and step precisely.<br/>
Do **not** continue after something fails!" %}

## Basic requirements


1. Read through the instructions at least once before actually following them, so as to avoid any problems due to any missed steps!
2. Make sure your computer has `adb`{% unless device.install_method == 'heimdall' or device.install_method == 'dd' %} and `fastboot`{% endunless %}. Setup instructions can be found [here]({{ "help/adb-fastboot-guide/" | relative_url }}).
3. Enable [USB debugging]({{ "help/adb-fastboot-guide/#setting-up-adb" | relative_url }}) on your device.
{%- if device.models %}
4. Make sure that your model is actually listed in the "Supported models" section [here]({{ "devices/" | append: device.codename | append: "#supported-models" | relative_url }}) (exact match required!)
{%- endif %}
5. Boot your device with the stock OS at least once and check every functionality.
  Make sure that you can send and receive SMS and place and receive calls (also via WiFi and LTE, if available), otherwise it won't work on PixelExperience either!
6. PixelExperience is provided as-is with no warranty. While we attempt to verify [everything works](https://github.com/PixelExperience/docs/blob/master/device_requirements.md) you are installing this at your own risk!

{%- if device.before_install %}
{% capture path %}templates/device_specific/before_install_{{ device.before_install }}.md{% endcapture %}
{% include {{ path }} %}
{%- endif %}

{% if device.required_bootloader %}
## Special requirements

{% capture bootloader %}
Your device must be on bootloader version {% for el in device.required_bootloader %} {% if forloop.last %} `{{ el }}` {% else %} `{{ el }}` / {% endif %} {% endfor %}, otherwise the instructions found in this page will not work.
The current bootloader version can be checked by running the command `getprop ro.bootloader` in a terminal app or an `adb shell` from a command prompt (on Windows) or terminal (on Linux or macOS) window.
{% endcapture %}
{% include alerts/warning.html content=bootloader %}
{% endif %}

<script>
$(function() {
  if (window.location.hash.length === 0) {
    toggleBlur()
  }
})

function toggleBlur() {
  $('#blurred').toggleClass('blurred')
  $('#unblur').toggle()
}
</script>

<div id="unblur" style="display: none;">
  By clicking the following button you are confirming that you've met all of the basic requirements and read the warnings.<br/>
  <button onclick="toggleBlur()" class="btn btn-primary">Show instructions</button>
</div>

<div id="blurred" markdown="1">

{% if device.install_method %}
{% capture recovery_install_method %}templates/recovery_install_{{ device.install_method }}.md{% endcapture %}
{% include {{ recovery_install_method }} %}
{% else %}
## Unlocking the bootloader / Installing a custom recovery

There are no recovery installation instructions for this discontinued device.
{% endif %}

{% if device.before_install_custom %}
{% capture path %}templates/device_specific/before_install_custom_{{ device.before_install_custom }}.md{% endcapture %}
{% include {{ path }} %}
{% endif %}

## Installing PixelExperience from recovery

1. Download the [PixelExperience installation package](https://download.pixelexperience.org/{{ device.codename }}) that you would like to install or [build]({{ "devices/" | append: device.codename | append: "/build" | relative_url }}) the package yourself.
2. If you are not in recovery, reboot into recovery:
    * {{ device.recovery_boot }}
    {% if device.vendor == "LG" %}
        {% include templates/recovery_boot_lge.md %}
    {% endif %}
{% if device.uses_custom_recovery %}
3. Now tap **Wipe**.
4. Now tap **Format Data** and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage.
5. Sideload the PixelExperience `.zip` package:
    * On the device, select "Advanced", "ADB Sideload", then swipe to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/specific/tip_adb_flash_success.html %}
{% else %}
3. Now tap **Factory Reset**, then **Format data / factory reset** and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage, as well as format your cache partition (if you have one).
4. Return to the main menu.
5. Sideload the PixelExperience `.zip` package:
    * On the device, select "Apply Update", then "Apply from ADB" to begin sideload.
    * On the host machine, sideload the package using: `adb sideload filename.zip`.
        {% include alerts/specific/tip_adb_flash_success.html %}
{% endif %}
{% if device.uses_custom_recovery %}
8. Once you have installed everything successfully, run 'adb reboot'.
{% else %}
8. Once you have installed everything successfully, click the back arrow in the top left of the screen, then "Reboot system now".

Note:- If you get error 7 while sideloading:
1. Download [super_empty.img](https://wiki-blobs-dl.pixelexperience.org/wiki_blobs_martini/main/android-13/super_empty.img).
2. Reboot to fastbootD 
3. Use command `fastboot wipe-super super_empty.img`
4. Now you can sideload rom, Don’t forget to format data after sideloading.

{% endif %}

{%- capture first_boot %}
The first boot usually takes no longer than 15 minutes, depending on the device.
If it takes longer, you may have missed a step, otherwise feel free to [get assistance](#get-assistance).
{%- endcapture %}
{% include alerts/note.html content=first_boot %}

{% if device.custom_recovery_link or device.uses_custom_recovery %}
{% include alerts/specific/warning_recovery_app.html %}
{% endif %}
{% include alerts/specific/tip_sideload_stuck_47.html %}


{% if device.after_install_custom %}
{% capture path %}templates/device_specific/after_install_custom_{{ device.after_install_custom }}.md{% endcapture %}
{% include {{ path }} %}
{% endif %}

## Get assistance

After you've double checked that you followed the steps precisely, didn't skip any and still have questions or got stuck, feel free to ask on [our Telegram group](https://t.me/pixelexperiencechat).

</div>
