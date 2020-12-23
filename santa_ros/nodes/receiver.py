#!/usr/bin/env python

import rospy

from haxmas-ros.msg import Santa.msg

class Receiver:

    def __init__(self):

        self.message_sub = rospy.Subscriber('/message', String, msg_cb, queue_size=10)

    def msg_cb(self, data):


def main():

    receiver = Receiver()

if __name__=='__main__':
    main()