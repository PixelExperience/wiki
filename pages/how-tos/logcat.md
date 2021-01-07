---
sidebar: home_sidebar
title: How to capture logs
folder: how-tos
permalink: help/logcat/
tags:
 - how-to
---

## Taking logs for bug reports

These instructions will generate a `logcat` file which you can then attach to a [bug report]({{ site.baseurl }}/help/bugreport/#reporting-a-bug).
That file basically consists of a log of system messages, including stack traces when the device throws an error, and debug messages from apps.

### With a computer

{% capture content -%}
This method requires that you have [`adb` installed]({{ site.baseurl }}/help/adb-fastboot-guide).
If you don't have it installed, please do that before continuing.
{% endcapture -%}

{% include alerts/note.html content=content %}

1. Open Command Prompt (Windows) or Terminal (Linux/macOS).
2. Connect your device via cable or [over WiFi]({{ site.baseurl }}/help/adb-over-wifi)
3. Type `adb logcat -d > logcat.txt`. This will save the log to `logcat.txt`.

   Additionally, the radio buffer can be viewed or stored with `logcat`. If needed or requested, type `adb logcat -db radio > radio.txt` to save it to `radio.txt`.

### On your device

{% include alerts/note.html content="This method requires that your device is rooted." %}

1. Install and open some Terminal app, we recomend that: [https://play.google.com/store/apps/details?id=yarolegovich.materialterminal](https://play.google.com/store/apps/details?id=yarolegovich.materialterminal)
2. Type `su` and confirm root access - you may have to turn on root access for apps in **Developer options**.
3. Type `logcat -d -f /sdcard/logcat.txt`. This will save the log to `/sdcard/logcat.txt`.

   Additionally, the radio buffer can be viewed or stored with `logcat`. If needed or requested, type `logcat -db radio -f /sdcard/radio.txt` to save it to `/sdcard/radio.txt`.
