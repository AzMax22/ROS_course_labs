#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3


def process_msg(msg):
    msg.x, msg.y, msg.z = msg.x**3, msg.y**2, msg.z 


def callback(msg):
    rospy.loginfo(f"{rospy.get_name()}: I get v3 - {msg}")

    process_msg(msg)

    rospy.loginfo(f"{rospy.get_name()}: I create  - {msg}")

    pub.publish(msg)


rospy.init_node("polynom")
pub = rospy.Publisher("v3_pow", Vector3, queue_size=10)
rospy.Subscriber('v3', Vector3, callback, queue_size=10)


rospy.spin()


