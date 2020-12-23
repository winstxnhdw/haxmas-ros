#!/usr/bin/env python

import rospy
import json

from santa_ros.msg import Elves

class Publisher:

    def __init__(self):

        self.message_pub = rospy.Publisher('/message', Elves, queue_size=10)

        try:
            self.message_path_params = rospy.get_param("/PATH/JSON")
            self.message_path = self.message_path_params

        except:
            raise Exception("Missing ROS parameters. Check the launch file.")

        with open(self.message_path, "r") as read_file:
            debug_dict = json.load(read_file)

        self.reply = debug_dict['reply']
        self.sentiment = debug_dict['sentiment']

    def publish_letter(self):

        letter = Elves()
        
        letter.reply = self.reply
        letter.sentiment = int(self.sentiment)

        self.message_pub.publish(letter)

def main():

    publisher = Publisher()

    rospy.init_node('debug_publisher')

    try:
        publisher.publish_letter()

        rospy.spin()
    
    except KeyboardInterrupt:
        print("Shutting down..")

if __name__=='__main__':
    main()