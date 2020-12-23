#!/bin/bash

# exit when any command fails
set -e

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG

# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

# other apt-get installs
sudo apt-get install git -y

# pip installs
pip install --upgrade pip
pip install playsound
pip install gpiozero