---
sidebar: home_sidebar
title: How to connect to adb over wifi
folder: how-tos
permalink: help/adb-over-wifi/
tags:
 - how-to
---

In some cases it might be required to get adb access to your device without plugging in a cable:
  - Charging port is in bad shape
  - The data cable is broken
  - The cable is in another room and you are a couch-potato

{% include alerts/important.html content="Make sure no device is connected to your computer via cable,
otherwise any command used after connection won't get through to the correct device" %}

{% include alerts/note.html content="This method is supported natively since Android 11." %}

## Steps

### On your device

1. Go to the developer settings
2. Press `Enable Wireless debugging`
3. Select `Pair device with pairing code`

You will see a dialog showing you IP address, port and a code.

### On your computer

1. Open a command line window
2. Type `adb pair <ip>:<port>` and replace `<ip>` and `<port>` with the data seen on the device
3. You will be asked for the pairing code. Type it in and hit <key>Enter</key>
4. You will now see an output similar to
```Successfully paired to <ip>:<port>```
5. To connect to the device, type `adb connect <ip>:<port>` and replace `<ip>` and `<port>` with the data seen on the Wireless debugging page after closing the pairing dialog

Additionally you will get a notification on your device.

{% include alerts/note.html content="This method is supported natively since Android 11." %}
