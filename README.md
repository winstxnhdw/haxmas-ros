# haxmas-ros
![Block Diagram](https://github.com/winstxnhdw/haxmas-ros/blob/main/screenshots/block.PNG)

## Abstract
HaXmas@EIG is a half-day hackathon, where teams develop a product under the theme of "Innovative Ways to Celebrate Christmas". The final product is a combination of a Telegram bot, AWS and ROS. This package contains the ROS component, which is responsible for interfacing with the relevant functions on the Raspberry Pi.

## Table of Contents
- [Abstract](#Abstract)
- [Relevant Packages](#Relevant-Packages)
- [Requirements](#Requirements)
  - [Hardware](#Hardware)
  - [Operating System](#Operating-System)
  - [Software](#Software)
- [Quick Start](#Quick-Start)


## Relevant Packages
- [ROS Bridge](https://github.com/khayliang/haxmas-bridge)

## Requirements
### Hardware
- Raspberry Pi 4 Model B
- LEDs x3

### Operating System
1. [Ubuntu 16.04.6 LTS (Xenial Xerus) or higher](http://releases.ubuntu.com/16.04/)

### Software
1. [Desktop-Full ROS Kinetic or higher](http://wiki.ros.org/kinetic/Installation/Ubuntu)
	 
2. [Python 2.7](https://www.python.org/download/releases/2.7/)
   - [pip](https://pypi.org/project/pip/)
   - [rospy](http://wiki.ros.org/rospy)
   - [playsound](https://pypi.org/project/playsound/)
   - [gpiozero](https://gpiozero.readthedocs.io/en/stable/installing.html)
   
3. [Git](https://git-scm.com/download/linux)

## Quick Start
Launch santa.launch
 - Launch your terminal
 - Type `catkin_make`
 - Type `roslaunch santa_ros santa.launch`
