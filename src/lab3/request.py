#!/usr/bin/env python3

# to set var use this:
# rosrun super_max_study_pkg request.py _x3:=10 _x2:=10 _x1:=10

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32

recieve_msg_flag = False


def send_req():
    x1 = rospy.get_param("~x1", 1)
    x2 = rospy.get_param("~x2", 2)
    x3 = rospy.get_param("~x3", 3)

    msg = Vector3()
    msg.x, msg.y, msg.z = x3, x2, x1

    pub.publish(msg)

    rospy.logout(f"Send x3={msg.x}, x2={msg.y}, x1={msg.z}")


def callback(msg):
    x1 = rospy.get_param("~x1", 1)
    x2 = rospy.get_param("~x2", 2)
    x3 = rospy.get_param("~x3", 3)

    rospy.logout(f"Result: {x3}**3 + {x2}**2 + {x1} = {msg.data}")

    global recieve_msg_flag 
    recieve_msg_flag = True


rospy.init_node("request")
pub = rospy.Publisher("v3", Vector3, queue_size=10, latch=True)
rospy.Subscriber("res", Float32,callback, queue_size=10)   


if __name__ == "__main__":
    # wait connection
    while pub.get_num_connections() < 1:
        rospy.sleep(0.5)
        send_req()   

    #wait recieve result msg
    while (not rospy.is_shutdown()) and (not recieve_msg_flag): 
        rospy.sleep(0.5)



    