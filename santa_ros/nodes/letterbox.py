#!/usr/bin/env python

import rospy

from santa_ros.msg import Elves
from utils.lights import *
from utils.speech import *

class Receiver:

    def __init__(self):

        self.letter_sub = rospy.Subscriber('/message', Elves, self.letter_cb, queue_size=10)

        self.sentiment = None
    

    def letter_cb(self, msg):
        
        def eventHandle(reply, sentiment):
            flash_switch = {
                0: flash_green(),
                1: flash_orange(),
                2: flash_all(),
                3: flash_red()
            }
            flash_switch.get(sentiment)
            
            audio_switch = {
                0: speak(reply, 'good'),
                1: speak(reply, 'neutral'),
                2: speak(reply, 'mixed'),
                3: speak(reply, 'bad')
            }
            audio_switch.get(sentiment)

        eventHandle(msg.reply, msg.sentiment)

def main():

    receiver = Receiver()

    rospy.init_node('letterbox')

    try:
        eventHandle(receiver.reply, receiver.sentiment)

    except:
        pass

    try:
        rospy.spin()
    
    except KeyboardInterrupt:
        print("Shutting down..")

if __name__=='__main__':
    main()