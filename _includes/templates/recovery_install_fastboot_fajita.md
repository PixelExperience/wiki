{%- assign device = site.data.devices[page.device] -%}
## Now let's install PixelExperience on our device!

### Make sure you have:
1. Unlocked the bootloader
2. Upgraded to OOS 11 / H2OS 11
3. Initialized dynamic partitions

### 1.Reboot to bootloader
### 2.Boot a Recovery designed for handling dynamic partitions
#### Download it from here
[Download special recovery](https://sourceforge.net/projects/sn-roms/files/TWRP/TWRP-3.7.0_12-fajita-2.img/download)
```
fastboot devices
fastboot boot xxx.img
```
### 3.Format userdata partition
### 4.Flash the ROM
Use adb sideload
```
adb sideload PixelExperience_Plus_fajita-13.0-yyyymmdd-xxxx-OFFICIAL.zip
```
### 5.Reboot and ... enjoy yourself!!
