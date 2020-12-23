#!/usr/bin/env python

import rospy

from santa_ros.msg import Elves

class Receiver:

    def __init__(self):

        self.letter_sub = rospy.Subscriber('/message', Elves, self.letter_cb, queue_size=10)

    def letter_cb(self, msg):

        rospy.loginfo(msg.reply)
        rospy.loginfo(msg.sentiment)

def main():

    receiver = Receiver()

    rospy.init_node('letterbox')

    try:
        rospy.spin()
    
    except KeyboardInterrupt:
        print("Shutting down..")

if __name__=='__main__':
    main()