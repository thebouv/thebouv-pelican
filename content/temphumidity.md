Title: Temperature and Humidity Sensors (part one)
Date: 2021-03-18
Category: homelab
Summary: I have a home from 1914 which has a lot of charm and a lot of issues. One of which is the need to constantly pay attention to the humidity levels and temperature in all floors, finished and unfinished, in the house. This project of my homelab will cover the hardware and custom software I write for it.
Tags: homelab, raspberrypi

## Setting Up

I have a home from 1914 which has a lot of charm and a lot of issues. One of which is the need to constantly pay attention to the humidity levels and temperature in all floors, finished and unfinished, in the house. This project of my homelab will cover the hardware and custom software I write for it.

### Hardware

4x Raspberry Pi Zero WH (just like the W, but with pre-soldered headers on the GPIO)  
4x Raspberry Pi official zero w cases
4x Raspberry Pi official power supplies
4x Gigastone 16gb MicroSDHC

### Operating System

Though I wish I could use Ubuntu LTS on the Pi Zero W, it doesn't seem to be supported or I at least haven't been able to find out how to boot it. Like my pihole project for the lab, I'm using the most recent official Raspberry Pi OS Lite (because I don't want a desktop environment on this headless computer). And of course I use the Raspberry Pi Imager -- it's just really convenient.

After I image the SD card I make a couple changes to the config.txt file on the card itself from the host machine I did the imaging from.  This is so I can set the gpu mem split and disable bluetooth.

>>>Note: when the Raspberry Pi imager is done it unmounts the SD card, so you'll need to plug it back in to your host machine to edit the config.txt file.  On my Mac, it mounts as *boot*.

I add these two lines config.txt. There are a couple of lines that already set dtoverlay that are commented out, so I just put both of these in that area:  

```
gpu_mem=16
dtoverlay=disable-bt
```

### Wi-Fi

I also want to go ahead and set up the wifi on the pi zero so that when I turn it on it automatically connects.

Following this [tutorial](https://learn.adafruit.com/raspberry-pi-zero-creation/text-file-editing) I create the *wpa_supplicant.conf* file on the root level of the boot drive while the SD is still connected.

### SSH

SSH is disabled by default so since I want to log in soon after booting it and stay headless, I merely need to add a blank file named *ssh* to the root level of the ssd that I still have mounted.

Once I've done that I eject the SD card and install it into the pi zero.

## First Boot

After I first boot, I want to make sure to make some changes to each device. There's probably a way to get fancy and make this super repeatable, but I'm not installing 100 sensors; I'm installing 4.

### Wrap Up Setup

I find the device on my network by looking at my Unifi OS that shows the whole network as a map and I just found the device and ip there, but I could also scan the network from the command line and look for Raspberry Pi MAC addresses:

```
arp -a | grep -i "b8:27:eb\|dc:a6:32"
```

Or if you're on a Mac or a Windows machine that has Bonjour set up you might be able to talk to it at its default hostname on .local via *raspberrypi.local*

```
ssh pi@ip.address.you.found
# or 
ssh pi@raspberrypi.local
``` 

>>>WARNING: If you use ssh pi@raspberrypi.local more than once because you're setting up multiple sensors, keep in mind ssh is going to complain that raspberrypi.local doesn't match the fingerprint from the last time you did it. Cause each device you set up is unique, but ssh doesn't know that. So I suggest using the IP because it is more likely to be different. And below we're giving each their own hostname anyway.

Change the default password (always a smart thing to do):

```
passwd
```

Update apt and upgrade the OS packages:

```
sudo apt update && sudo apt upgrade -y
```

Update the hostname. I'm going with a naming scheme of 'temphum1', 'temphum2', etc.

```
sudo vi /etc/hostname
```

And now let's shut it down for now because we're going to be installing the sensor and doing some soldering next before we turn this device back on.

The part two of this post will be abour the physical aspects of the project like testing out on a breadboard and soldering the real thing together.