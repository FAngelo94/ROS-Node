#!/usr/bin/env python

"""
Simple node for testing the Python ROS libraries.
"""

import rospy
from std_msgs.msg import String

def callback(msg):
    print(msg)

def main():
    rospy.init_node("listener", anonymous=True)

    sub = rospy.Subscriber("chatter", None, callback)

    rospy.spin()

if __name__ == '__main__':
    main()
