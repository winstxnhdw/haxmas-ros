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

            if sentiment == 0:
                flash_green()
                speak(reply, 'good')

            elif sentiment == 1:
                flash_orange()
                speak(reply, 'neutral')

            elif sentiment == 2:
                flash_all()
                speak(reply, 'mixed')

            elif sentiment == 3:
                flash_red()
                speak(reply, 'bad')

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