---
sidebar: home_sidebar
title: How to submit a new device for official builds
folder: internal
permalink: help/adding-device/
search: exclude
tags:
 - internal
---

## Official devices

If you have a working device tree/kernel, and would like to submit it for official builds, please check [this url](https://github.com/PixelExperience/official_devices/blob/master/README.md) for more instructions. Please note - your device **must** have full hardware support (i.e., every peripheral works) and **must** be stable.

The PixelExperience wiki provides instructions based on the assumption that your device has got its device tree and required depedencies under the [PixelExperience-Devices GitHub organization](https://github.com/PixelExperience-Devices).

## Setting up the wiki locally

See [this url]({{ site.baseurl }}/help/contributing/wiki/) for detailed instructions on setting up the wiki locally.

## Adding your device

### Prepare the required files

There are a few files which need to be there to have a device on the wiki.
In order to get them, navigate to `~/wiki/` and run:

```
./scripts/generate_device.sh your_device
```

Obviously replace `your_device` with the codename of your device

### Populating the YAML

The sample template has been copied to `~/wiki/_data/devices/your_device.yml`.
Update the values to match your device. An explanation of some of the options is below:

{% assign definitions = site.data.schema.definitions %}
{% assign properties = site.data.schema.properties %}

* `architecture`: The CPU architecture of the device, can be one of

  ```
  {{ definitions.valid_architectures.enum | join: ', ' }}
  ```

  If your device has a 64 bit architecture but Android runs on 32 bit, you can use a different format: `{cpu: 'arm64', userspace: 'arm'}`

* `battery`: Use the format `{removable: False, capacity: <number in mAh>, tech: '<tech>'}`. If your battery is removable, use `True` instead.
For `tech` you can use:

  ```
  {{ definitions.battery_data.properties.tech.enum | join: ', ' }}
  ```

  In case you are setting up one file for multiple devices which have different batteries, you can use Model-Value-Pairs, e.g.

  ```
  battery:
  - Model1: {removable: False, capacity: 1000, tech: 'Li-Ion'}
  - Model2: {removable: True, capacity: 2000, tech: 'Li-Po'}
  ```

* `bluetooth`: The proper format is either `{spec: '<version>'}` with `version` being the version of the BT protocol supported, or `{spec: '<version>', profiles: '<profiles>'}` when your device
  supports additional profiles. These are the possible values:

  ```
  For the specification:
  {{ properties.bluetooth.properties.spec.enum | join: ', ' }}

  For the optional profiles:
  {{ properties.bluetooth.properties.profiles.items.enum | join: ', ' }}
  ```

* `cpu`: The CPU type of the device, can be one of the following list:

  ```
  {{ properties.cpu.enum | join: ", " }}
  ```


* `download_boot`: Instructions for booting the device into the mode used to install recovery. On most devices, this is fastboot mode.
* `install_method`: Used to determine the recovery install template to use. Templates can be found in \_includes/templates/recovery\_install\_`install_method`.md.
* `network`: The frequencies and channels for the various network technologies. You can look them up [here](https://www.frequencycheck.com/models/). Keep the non-available technologies empty.
* `peripherals`: A list of peripherals available on the device, can be any of the following list:

  ```
  {{ definitions.valid_peripherals.items.enum | join: ", " }}
  ```

* `release`: Allowed formats are `yyyy`, `yyyy-mm` and `yyyy-mm-dd`. In case of multiple devices with different dates, you can use Model-Value-Pairs:

  ```
  release:
  - Model1: 2015
  - Model2: 2016-01
  - Model3: 2016-02-01
  ```


Additionally there are some optional properties which you might not need, but in case you do, they are documented below:

* `carrier`: If the device was released for a specific carrier, the name of that carrier. Remove this if not used!
* `custom_recovery_link`: A custom recovery link in case no official recovery exists for the specific device or it doesn't work properly. Remove this if not used!
* `custom_recovery_codename`: If an official recovery exists for the device, but it uses a different codename, specify the used one here. Remove this if not used!
* `custom_unlock_cmd`: Used if the command to unlock your device via fastboot is different than `fastboot oem unlock`. Remove this if not used!
* `format_on_upgrade`: Used if the device needs to wiped on major PixelExperience version due to unfixable device specific issues. Remove if not used!
* `is_ab_device`: Used if the device has an A/B partition scheme. Remove this if not applicable to your device!
* `is_unlockable`: Set to false if there is no official method to unlock the bootloader. A hint will appear on the device's overview and install page. If this property is not set, it defaults to `True`
* `required_bootloader`: Specify the bootloader versions which are required to install PixelExperience. If no special requirement exists, remove this line! Example:

  ```
  required_bootloader: [Version1, Version2]
  ```

* `uses_twrp`: Used if the device doesn't use PixelExperience Recovery (the default)

{% include alerts/note.html content="If you need to assign a value to one of the fields which is not allowed by the time you create your change, update the schema validator or contact us to add it" %}

## Testing it works

Start the wiki on your local Jekyll server, and navigate to [the devices list](http://localhost:4000/devices.html). Your device should be there.
Click on it, and check that the info/install/build pages all seem correct.

Now run the validation:

```
bundle install
ruby ./test/validate.rb
```

If the script doesn't give you an output, all the validated fields have a proper format. Otherwise, read the messages carefully to see which fields have to be corrected.

## Submitting wiki changes

After verifying the device-specific pages, commit it and open a pull request at [wiki source code](https://github.com/PixelExperience/wiki/) to review proposed changes.
