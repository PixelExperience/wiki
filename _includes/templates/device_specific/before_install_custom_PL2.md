## Ensuring all firmware partitions are consistent [2/4 - Optional] :

{% include alerts/note.html content="The steps below only need to be run once per device." %}

1. Download the latest firmware from [Here](https://sourceforge.net/projects/fihsw-sdm660/files/PL2/FIHSW_PL2-415C-0-00WW-B01_600WW_10_20200501.full.lzma2.8196b83ea498b17a172bbb95f46b94cb3bab32404f2493a818e390f858a55eaf.7z/download)
2. Download the `HCTSW Care OSTRemote Client tool` & follow the usage/flashing guide from [Here](https://xdaforums.com/t/tools-hctsw-care-ostremote-client-batch-script-replacement-of-ost-la.4282019/).
3. Once the firmware installation is done, now power off the device & follow up the below steps.

## Retrofit Dynamic Partititions instruction [3/4] :

{% include alerts/warning.html content="Retrofit Dynamic partition must be initialized when installing for the first time, so the process to do so is described below." %}

1. Reboot your device into `Download mode/fastboot mode`
2. Install the `Nokia Driver` from [Here](https://github.com/StollD/nokia-driver-installer/raw/master/out/Phone_Nokia_USB_Driver_v1.4.0.exe)
3. Download `PLatform tool by Google` from [Here](https://developer.android.com/tools/releases/platform-tools)
4. Download the `super_empty.img` from [Here](https://github.com/Nokia-SDM660-Devices/device_nokia_PL2/releases/download/PL2-RDP/super_empty.img)
5. Now flash `super_empty.img` file with the given command
```fastboot wipe-super <PATH TO Super-empty.img>```
6. Now follow up with the below steps.

## ROM installation [4/4] :

1. Reboot your device into `fastboot mode/Download mode`
2. Type `fastboot device`, if the device S/N detected then everything is all good. [If not detected install the [Nokia Driver](https://github.com/StollD/nokia-driver-installer/raw/master/out/Phone_Nokia_USB_Driver_v1.4.0.exe) & [Platform tool](https://developer.android.com/tools/releases/platform-tools)]
3. Now flash the boot.img (PixelExperice recovery) in both the slots by the following commands:
```
fastboot flash boot_a <PATH_TO_boot.img>
fastboot flash boot_b <PATH_TO_boot.img>
```
4. Now reboot into `recovery mode` by holding the Volume Up & Power button.
5. Apply Update >> adb sideload method & sideload the PixelExperience .zip file by `adb sideload <PATH_TO_PixelExperience-*.zip>`
6. Once the installation done, perform the `Factory reset` then >> `Reboot to system`