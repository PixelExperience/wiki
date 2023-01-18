## Before Installing Rom

{% include alerts/warning.html content="Make sure you are on OxygenOS 12.1 C07 before installing anything on your device, Steps to do so is" %}

## If you are below OxygenOS13 (F.13)
1. Download OxygenOS 13.0 F.13 from [here](https://sourceforge.net/projects/playground0230/files/OOS13/388b8e01f4364918a9e96543061710b8.zip/download).

2. Install the above via local updater in settings

3. Let the update boot itself, After device boots, You will need to flash the same file again (making it two times in total)

Note. Enable developer options and usb debugging if local update option doesn't show up in settings.

4. You can proceed with next steps now.

## If you are already on OxygenOS13 (F.13)
5. Download OxygenOS 13.0 F.13 from [here](https://sourceforge.net/projects/playground0230/files/OOS13/388b8e01f4364918a9e96543061710b8.zip/download).

6. Install the above via local updater in settings

## For users on PE with oos12.1 as base
7. Download and extract fastboot rom of oos12.1 from [here](https://androidfilehost.com/?fid=4279422670115706121)

8. Before flashing fastboot rom, flash dtbo.img (in img folder),
Use command fastboot flash dtbo dtbo.img

9. Now you can install fastboot rom using install.bat 

Note:- If device doesn't boots into fastbootD, redo step 7
