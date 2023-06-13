## Before Installing PixelExperience

{% include alerts/warning.html content="When installing PixelExperience for the first time you'll need to retrofit dynamic partitions. The process is described step by step below. If your device is already retrofitted, you can skip this step." %}

1. Download [this](https://gitlab.pixelexperience.org/android/vendor-blobs/wiki_blobs_chiron/-/raw/main/android-13/super_empty.img?inline=false) `super_empty.img` file.
2. In PixelExperience recovery go to `Advanced` -> `Enter Fastboot`
3. Now initialize the retrofit by using the following command on your PC
```
fastboot wipe-super super_empty.img
```
4. Now you can go back to the main recovery screen and continue installation.
