---
sidebar: home_sidebar
title: Frequently Asked Questions
permalink: help/faq/
---

## Installing PixelExperience zips in Recovery results in "Error 7"
 - The most common reasons for this error are:
   - You are trying to install a build for a different device. _You need to make sure you download the zip for the correct device *and* variant_
   - You are attempting to migrate from an unofficial build to official PixelExperience. _A full data wipe is needed if you are coming from something other than an official build of PixelExperience._
   - Your vendor/modem/bootloader is too old (or maybe too new). _Flash the correct stock image for your device, before wiping data and attempting to install PixelExperience again_. This information should be listed on the device's wiki page.
   - Your recovery is outdated. _Flash the newest available version of the recommended recovery image for your device_.
 - If your error still persists after confirming these are not causing your issue, ask someone for help on [our Telegram group](https://t.me/pixelexperiencechat) and provide a recovery log.
<!--  -->
## My device _is_ officially supported, but there's no zips for it on the download page. Where are they?
 - Be patient. Maintainers have busy lives, and sometimes an issue is holding it back. Please do not ask for ETAs.

## My device is _not_ officially supported, but I'd really like to give PixelExperience a try. Can you support my device?
 - All devices are maintained by open source contributors - [sorry, we don't take device requests]({{ "help/device-requests/" | relative_url }}). If you would like to bring-up PixelExperience for a device, and can meet some basic standards, we'll happily look into making it official.
 - If you have a working device tree/kernel, and would like to submit it for official builds, please check [this url](https://github.com/PixelExperience/official_devices/blob/master/README.md). Please note - your device **must** have full hardware support (i.e., every peripheral works) and **must** be stable.

## A build for my device disappeared? Where'd it go?
 - Occasionally a build is broken. If this happens, we remove it until the next build cycle. It is also possible the device is no longer in the official build roster and its old builds are being purged, or that the version it supported is no longer supported. You can check your device's wiki page to confirm support status.

## Where can I find the last build for _xxx_ device before support was dropped/its PixelExperience version was deprecated?
 - In short, you can't. We don't keep building, or keep builds around for any older version (e.g. when ten builds started, pie builds stopped and the builds were slowly removed). We don't keep old builds around for a multitude of reasons, the largest being that we won't keep old, insecure, potentially broken builds around. Additionally, we don't have the server space (or the space on mirrors) to do so.

## What is the difference between full packages and incremental packages?
 - Full packages - are normal zip packages containing all files of the PixelExperience software, which is usually large.
 - Incremental packages - also known as a delta update, is a package that contains only changes from the last official build. Therefore, this file is generally much smaller compared to the full package.

## I found a bug. What do I do?
 - You can report it! Please _carefully_ read the [How to submit a bug]({{ "help/bugreport/" | relative_url }}) page before reporting it.

## Can I have _xxx_ feature added?
 - Don't ask.

## Where does the updater app store the downloaded zip?
 - `/data/system_updates/`
