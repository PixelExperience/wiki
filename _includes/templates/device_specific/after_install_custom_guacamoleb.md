## Post-install instructions

The steps below are recommend but are completely OPTIONAL.

It is recommended to flash [this file](https://www.arter97.com/browse/f2fs/optimize/20190607/f2fs-optimize.zip) after first boot, to ensure best F2FS Performance.

Flash the file after booting into recovery, once your basic device setup is done.

On guacamoleb, you can also relock your bootloader to gain Widevine L1 certification.

{% include alerts/warning.html content="Your data will be lost, please do a backup." %}

1. Make sure your device is in bootloader/fastboot mode.
2. Download the PixelExperience avb_custom_key Image from [Here](https://github.com/PixelExperience-Devices/blobs/raw/main/avb_custom_key.img)
3. Flash the '.img' file via fastboot:
    * On the device, be in bootloader/fastboot mode.
    * From the host machine, flash the image using: `fastboot flash avb_custom_key avb_custom_key.img`
4. Now you can lock your bootloader using: `fastboot oem lock`
