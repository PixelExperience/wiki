---
sidebar: home_sidebar
title: Contributing to the wiki
folder: meta
permalink: help/contributing/wiki/
---
So, you've decided you want to edit the wiki. Awesome! This page will show you how to get started. Please follow the instructions that are most appropriate for you.

## Cloning the wiki

#### Install Git

##### On Windows

Install [Git for Windows](https://git-for-windows.github.io/).

##### On macOS

Install Git using the [Git installer](https://git-scm.com/download/mac).

##### On Linux

You can install Git by running:

```
sudo apt-get install git
```

More specific instructions for different distributions can be found [here](https://git-scm.com/download/linux).

#### Configure Git

Run:

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

{% include alerts/tip.html content="Before this step, you can fork the PixelExperience wiki repository and work on your own copy. That way you can preview your changes online using GitHub pages, which [we've detailed below](#preview-using-github). Just fork the repo and then replace PixelExperience in the `git clone` command with your GitHub username." %}

```
git clone https://github.com/PixelExperience/wiki ~/wiki
cd ~/wiki
```

## Making and previewing changes

You can now make changes in this folder using your favorite text editor. If you ever need to reset your folder to a known-good state, erasing your changes, just run:

```
git reset --hard HEAD
```

### Preview using GitHub

This is probably the easiest method, but requires you to have forked the wiki repository, and have cloned from that.

#### Commit and preview your changes

Run:

```
git add .
git commit
```

An editor will pop up. In the first line, type a short (below 80 character) description of your changes,
then put a blank line, and, if you want, a more detailed description of your changes. For example:
```
Add the contributing page

The contributing page will show people how they can edit our wiki, which
is important, since it wouldn't be much of a wiki without editors.
```
Save the file and exit the editor. Now upload your changes to GitHub:

```
git push origin
```

Preview your changes - you can see your fork of the wiki at `http://yourusername.github.io/wiki`.

#### Fixing mistakes

So, you've made your change, and you can look at the wiki on GitHub pages. But something's wrong!
You made a typo - or accidentally deleted something. Have no fear! You can fix it.

First, fix the mistake(s) you made. Then, to push them to GitHub:

```
git add .
git commit --amend
```

Your commit message should show up in an editor. You can edit it, or just quit the editor.
Finally, run:

```
git push --force origin
```

### Preview locally using docker

{% include alerts/warning.html content="Docker requires a 64 bit OS. If you do not have a 64 bit OS, do not continue." %}

#### Install docker

Add docker keyring and install the package:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce
```

Add your user account to the _docker_ group in order to use docker commands without prefixing `sudo`:

```
sudo gpasswd -a $USER docker
newgrp docker
```

Then log out of your user account and log back in or reboot to make the group membership changes take effect.

#### Build the docker image

This builds the docker image, which should only need to be done once:

```
cd ~/wiki
docker build -t pixelexperience/wiki .
```

#### Edit the wiki

Each time that you want to edit the wiki, you will need to start a local web server running Jekyll:

```
cd ~/wiki
docker run -p 4000:4000 -v $(pwd):/src -it pixelexperience/wiki
```

At this point you should be able to view the [local Jekyll server](http://127.0.0.1:4000).

### Preview locally using rvm and jekyll

#### Install `rvm`

`rvm` is a great tool to isolate different usages of ruby from each other. During this setup, you will install `ruby` and a set of ruby modules (gems) which will be isolated from any other ruby use on the machine (now and in the future).

If you don't have `rvm` already installed, go ahead and install it:

```
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable
```

#### Configure `ruby` for editing the wiki

These steps will configure and install the latest version of ruby MRI via `rvm`. All gems (modules) are stored in the namespace `wiki` and the environment will be configured to allow remote access to GitHub. Once configured, `ruby` will be installed and the required gems downloaded:

```
cd ~/wiki
echo ruby > .ruby-version
echo wiki > .ruby-gemset
rvm install ruby
gem install bundler rails
bundle install
```

#### Edit the wiki

Each time that you want to edit the wiki, you will need to start a local web server running Jekyll:

```
source ~/.rvm/scripts/rvm
cd ~/wiki
bundle exec jekyll serve --incremental
```

At this point you should be able to view the [local Jekyll server](http://127.0.0.1:4000).

{% include alerts/tip.html content="The incremental flag will cause Jekyll to only reprocess each page as you change it (without the incremental flag, it would reprocess the entire site which takes 10-30+ seconds depending on your hardware). This works very well when editing meta pages but is a little annoying when editing the data/device/name.yml files. When editing those files you will need to save the data and then touch the `.md` file of the page that you are viewing in the browser. An easy way to do that is: `touch pages/*/<devicename>*`" %}

{% include alerts/note.html content="If you work on a remote server and trust the network on which you are connected, you can add `--host <fully-qualified hostname>` to the Jekyll command line to allow remote connections to the server." %}


## Uploading your changes

You need to open a pull request at [Github](https://github.com/PixelExperience/wiki/) to review proposed changes.
