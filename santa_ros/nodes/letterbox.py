#!/usr/bin/env python

import rospy

from santa_ros.msg import Elves
from utils.lights import *
from utils.speech import *

class Receiver:

    def __init__(self):

        self.letter_sub = rospy.Subscriber('/message', Elves, self.letter_cb, queue_size=10)

        try:
            self.audio_path_params = rospy.get_param("/PATH/AUDIO")
            self.audio_path = self.audio_path_params

        except:
            raise Exception("Missing ROS parameters. Check the launch file.")

        self.sentiment = None

    def letter_cb(self, msg):

        self.reply = msg.reply
        self.sentiment = msg.sentiment

def main():

    receiver = Receiver()

    rospy.init_node('letterbox')

    try:
        eventHandle(receiver.sentiment)

    except:
        pass

    try:
        rospy.spin()
    
    except KeyboardInterrupt:
        print("Shutting down..")

def eventHandle(sentiment):

    switcher =
    {
        0: flash_green(),
        1: flash_orange(),
        2: flash_all(),
        3: flash_red()
    }
    switcher.get(sentiment)

if __name__=='__main__':
    main()