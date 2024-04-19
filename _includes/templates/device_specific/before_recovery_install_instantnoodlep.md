## Flashing compatible firmware

{% include alerts/warning.html content="This device requires a disabled VBMeta image to be flashed prior to booting or flashing anything custom, the process to do so is described below." %}

1. Download [this](https://wiki-blobs-dl.pixelexperience.org/wiki_blobs_instantnoodlep/-/blob/main/android-13/vbmeta.img) `vbmeta.img` file.
2. Download [this](https://wiki-blobs-dl.pixelexperience.org/wiki_blobs_instantnoodlep/-/blob/main/android-13/dtbo.img) `dtbo.img` file.
3. Power off the device, and boot it into bootloader mode:
    * {{ device.download_boot }}
4. Flash a the downloaded images to your device by typing:
```
fastboot flash vbmeta vbmeta.img
fastboot flash dtbo dtbo.img
```
