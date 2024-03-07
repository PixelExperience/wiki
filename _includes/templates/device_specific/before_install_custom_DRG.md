## Unlocking the Bootloader [1/5] :

{% include alerts/note.html content="The steps below only need to be run once per device." %}
{% include alerts/warning.html content="Unlocking the bootloader will erase all data on your device!
Before proceeding, ensure the data you would like to retain is backed up to your PC and/or your Google account, or equivalent." %}

1. Install Nokia USB Drivers (required):
To ensure that your device is properly detected during the bootloader unlock process, make sure to install the required.
If you already have the required drivers installed you can skip this step. To install the drivers, download [this](https://github.com/StollD/nokia-driver-installer/blob/master/out/Phone_Nokia_USB_Driver_v1.4.0.exe) installer package from GitHub and install it to your computer.

2. Download and extract the Nokia Bootloader Unlock tool from [here](https://tchms.to/NokiaUBLTool). Using this tool you can easily unlock the bootloader of your device without touching the command line. Use a zip management tool of your choice to extract the tool to a folder on your computer.

{% include alerts/note.html content="The tool currently only supports Windows 7 or later with Microsoft .Net Framework version 4.7.2 or higher. Linux or Mac are not supported. Windows 10 with latest updates is recommended" %}

3. Reboot the phone into download mode:
Now you need to boot your device to download mode. Follow these steps for bootloader mode:

    1. Turn off your phone.
    2. Connect the USB cable to the device only and not the computer.
    3. Press and hold Volume Down + Power key together till you reach the screen reads that reads “Download mode”.
    Alternatively, you can also use the command ```adb reboot bootloader``` from the stock ROM to bring the phone to download mode.

4. Generate OTP for the Unlock Tool:
To avoid misuse and limit usage, the tool uses OTP (One-time password). Before you unlock you need to get an OTP. You can generate one from [here](https://www.techmesto.com/nokia-ubl-otp/)

{% include alerts/note.html content="The OTP is valid for only 15 minutes from generation. In addition only 15 devices are allowed for unlocking each day. After this further generation of OTPs will be disabled for the day. If the OTP generation fails, please be patient and wait for the next day to try again" %}

5. Run the Unlock Tool and unlock your phone
Now you can use the previously generated OTP to unlock the bootloader of your device.

    1. Run the "Bootloader Unlock by tm.exe" file in the folder where you extracted the tool
    2. Paste the OTP (from step 3) into the Enter OTP box in the Unlock Tool.
    3. Connect your smartphone in download mode.
    4. Click on the "BEGIN UNLOCK" button.
    5. Wait for the process to complete and follow the instructions shown in the output window.
    6. Your device should prompt you for unlock. Use the volume keys to accept the unlock

6. Once the device bootloader unlocked follow up with the next steps.