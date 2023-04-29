## Flashing RETROFIT ROM Guide

* How To Flash Using AOSP Recovery
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