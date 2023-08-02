## Flashing compatible firmware

{% include alerts/warning.html content="This device requires the vendor_boot, vbmeta, and dtbo images to be flashed prior to installing PixelExperience Recovery. The process to do so is described below." %}

1. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_dre/-/raw/thirteen/13/dtbo.img) `dtbo.img` file.
2. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_dre/-/raw/thirteen/13/vbmeta.img) `vbmeta.img` file.
3. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_dre/-/raw/thirteen/13/vendor_boot.img) `vendor_boot.img` file.
4. Power off the device, and boot it into bootloader mode:
   * {{ device.download_boot }}
6. Flash a the downloaded images to your device by typing:

```
fastboot flash dtbo dtbo.img
fastboot flash vbmeta vbmeta.img
fastboot flash vendor_boot vendor_boot.img
```
