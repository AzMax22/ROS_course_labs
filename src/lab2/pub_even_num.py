#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


rospy.init_node('pub_even_num')
even_pub = rospy.Publisher('even_num', String, queue_size=10)
overflow_pub = rospy.Publisher('overflow', String, queue_size=10)

rate = rospy.Rate(10) # 1 Hz


def publish_text(pub, text):
    msg = String()
    msg.data = text
    pub.publish(msg)

    rospy.loginfo(text)


def start_talker():
    i = 0

    while not rospy.is_shutdown():
        publish_text(even_pub, str(i * 2))
        i += 1
        if i * 2 > 100:
            publish_text(overflow_pub, "Overflow even numbers")
            i = 0

        rate.sleep()



try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')