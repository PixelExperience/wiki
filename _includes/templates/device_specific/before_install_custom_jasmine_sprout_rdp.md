## Pre-install instructions
For PixelExperience, you must flash the `Super_Empty.img` to make your device compatible for dynamic retrofit partition.

{% include alerts/note.html content="If you already have flashed Super_Empty.img and are using another ROM then you don't need to reflash it" %}

{% include alerts/note.html content="These steps needs to be done only once, and for first time installation only" %}

To flash Super_Empty.img head over to [THIS](https://github.com/PixelExperience-Devices/device_xiaomi_jasmine_sprout/releases/download/v1.0.0/super_empty.img) Link and download the `Super_Empty.img`.
1. Boot up PixelExperience recovery
2. Go to "Advanced" -> "Enter fastboot"
   {% include alerts/warning.html content="The \"Enter fastboot\" option may not be present on older PixelExperience recovery builds and it cannot be substituted with \"Reboot to bootloader\"." %}
3. And then in fastbootd[NOT FASTBOOT/BOOTLOADER] `fastboot wipe-super <super_empty>.img`. Now continue to flash the zip file normally
