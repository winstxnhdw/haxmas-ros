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
- [Installation](#Installation)
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

## Installation
1. Install [Ubuntu 16.04.6 LTS (Xenial Xerus) or higher](http://releases.ubuntu.com/16.04/)

2. Git clone this repository
   - Open your terminal
   - Go to the directory you wish to clone the repository in
   - Type `git clone https://github.com/winstxnhdw/haxmas-ros.git`
   
3. Change directory to your cloned path
   - Go to your terminal
   - Type `cd <workspace>/src/haxmas-ros`
   
4. Install [Desktop-Full ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)
   - Type `chmod +x ros-kinetic-desktop-full-install.sh`
   - Type `./ros-kinetic-desktop-full-install.sh` to install Desktop-Full ROS Kinetic
  
5. Install the required packages
   - Type `chmod +x requirements.sh`
   - Type `./requirements.sh` 

## Quick Start
Launch santa.launch
 - Launch your terminal
 - Type `catkin_make`
 - Type `roslaunch santa_ros santa.launch`
