## Post-install instructions
In some devices flashing a custom avb key to avb_custom_key is supported. Doing this will allow you to lock your bootloader. This step is OPTIONAL.

{% include alerts/warning.html content="Your data will be lost, please do a backup." %}

1. Make sure your device is in bootloader/fastboot mode.
2. Download the PixelExperience avb_custom_key Image from [Here](https://github.com/PixelExperience-Devices/blobs/raw/main/avb_custom_key.img)
3. Flash the '.img' file via fastboot:
    * On the device, be in bootloader/fastboot mode.
    * From the host machine, flash the image using: `fastboot flash avb_custom_key avb_custom_key.img`
4. Now you can lock your bootloader using: `fastboot oem lock`
