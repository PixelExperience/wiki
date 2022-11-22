## Flashing the dtbo and vendor boot partitions

{% include alerts/warning.html content="This platform requires the vendor boot partition to be flashed for recovery to work properly, the process to do so is described below." %}

1. Download [this]({{ device.vendor_boot_download_link }}) `vendor_boot.img` file and [this]({{ device.dtbo_download_link }}) `dtbo.img` file.
2. Power off the device, and boot it into bootloader mode:
    * {{ device.download_boot }}
3. Flash the downloaded images to your device by typing (replace `<dtbo>` and `<vendor_boot>` with the actual filename!):

```
fastboot flash dtbo <dtbo>.img
fastboot flash vendor_boot <vendor_boot>.img
```
