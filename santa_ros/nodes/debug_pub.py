#!/usr/bin/env python

import rospy
import json

from std_msgs.msg import String

class Publisher:

    def __init__(self):

        self.message_pub = rospy.Publisher('/message', String, queue_size=10)

        with open("../../debug.json", "r") as read_file:
            debug_dict = json.load(read_file)

        self.reply = debug_dict['reply']
        self.sentiment = debug_dict['sentiment']
        self.audio_url = debug_dict['audio']

def main():

    publisher = Publisher()

    rospy.init_node('debug_publisher')

    try:
        rospy.spin()
    
    except KeyboardInterrupt:
        print("Shutting down..")

if __name__=='__main__':
    main()