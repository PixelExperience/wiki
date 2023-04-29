## Flashing RETROFIT ROM Guide

{% include alerts/warning.html content="Follow the following guide to install PixelExperience 13 on mido using AOSP Recovery. Note: This in a RETROFIT build so follow the guide given below or you will be stucked."%}

1. Download the AOSP Recovery from the PE website
2. Copy the recovery to PC/laptop
3. Connect your device with PC/laptop (USB debugging should be turned on)
4. Reboot to fastboot 
5. Flash the recovery
6. Boot to recovery 
7. Format data using the recovery
8. On the device, select “Advanced”, “ADB Sideload”, then swipe to begin sideload.
9. On the PC/laptop, sideload the package using: adb sideload filename.zip
10. Format data
11. Reboot to system