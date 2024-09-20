#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32

rospy.init_node("summator")
pub = rospy.Publisher("res", Float32, queue_size=10)


def callback(msg):
    rospy.loginfo(f"{rospy.get_name()}: I get v3 - {msg}")

    msg_res = Float32() 
    msg_res.data = msg.x + msg.y + msg.z

    rospy.loginfo(f"{rospy.get_name()}: I create  - {msg_res}")

    pub.publish(msg_res)


rospy.Subscriber('v3_pow', Vector3, callback, queue_size=10)


rospy.spin()


