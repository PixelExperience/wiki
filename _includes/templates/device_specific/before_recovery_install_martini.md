## Before Flashing Rom

{% include alerts/warning.html content="This device needs Boot,Vendor_boot and dtbo from stock rom before flashing the rom,so the process to do so is described below." %}

1. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_martini/-/raw/main/android-13/boot.img?inline=false) `boot.img` file.
1. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_martini/-/raw/main/android-13/vendor_boot.img?inline=false) `vendor_boot.img` file.
2. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_martini/-/raw/main/android-13/dtbo.img?inline=false) `dtbo.img` file.
3. Power off the device, and boot it into bootloader mode:
    * {{ device.download_boot }}
4. Flash a the downloaded images to your device by typing:
```
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash dtbo dtbo.img
```
