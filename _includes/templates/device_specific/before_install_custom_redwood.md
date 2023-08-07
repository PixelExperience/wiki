## Flashing compatible firmware

1. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_redwood/-/raw/main/android-12/boot.img?inline=false) `boot.img` file.
2. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_redwood/-/raw/main/android-12/dtbo.img?inline=false) `dtbo.img` file.
3. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_redwood/-/raw/main/android-12/vendor_boot.img?inline=false) `vendor_boot.img` file.
4. Power off the device, and boot it into bootloader mode:
    * {{ device.download_boot }}
5. Flash a the downloaded images to your device by typing:
```
fastboot flash vbmeta boot.img
fastboot flash dtbo dtbo.img
fastboot flash vendor_boot vendor_boot.img
```.
