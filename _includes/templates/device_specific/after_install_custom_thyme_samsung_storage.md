## Post-install instructions
For some Mi 10S device which using Samsung flash memory, you need format data through bootloader.

{% include alerts/warning.html content="Your data will be lost, please do a backup." %}

1. Make sure your device is in bootloader/fastboot mode.
2. Format data using `fastboot -w`
3. Now you can reboot system using: `fastboot reboot`