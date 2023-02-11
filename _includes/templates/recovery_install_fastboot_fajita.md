# First time install
1. Download super_empty.img: 
https://sourceforge.net/projects/evolution-x/files/fajita/

2. Reboot to bootloader
3. Erase the old android partitions with the following:
``` fastboot erase system_a ```
``` fastboot erase system_b ```
``` fastboot erase odm_a ```
``` fastboot erase odm_b ```
``` fastboot erase vendor_a ```
``` fastboot erase vendor_b ```
4. Boot to recovery
5. In recovery, choose Advanced -> Enter fastboot to enter fastbootd
6. Initialize the retrofit super partitions for each slot:
``` fastboot wipe-super super_empty.img ```
``` fastboot set_active other ```
``` fastboot wipe-super super_empty.img ```
``` fastboot set_active other ```
7. Then enter our own modified TWRP or OrangeFox to install the ROM(https://sourceforge.net/projects/sn-roms) (don't flash recovery)

# Upgrade
1. Use Settings APP or use our own modified TWRP or OrangeFox
