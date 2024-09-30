#!/usr/bin/env python
import rospy
import tf
from tf.transformations import quaternion_from_euler
from  math import pi, cos, sin

rospy.init_node('tf_carrot')
dist = rospy.get_param('~dist', 1.5)
angle_vel = rospy.get_param('~angle_vel', 1) #in degree
parnt_frame = rospy.get_param('~parnt_frame', "turtle1")

angle_vel_rad = (angle_vel/180) * pi
i = 0

rate = rospy.Rate(60)



def publish_tf(br: tf.TransformBroadcaster):
    global i

    x = cos(i * angle_vel_rad) * dist
    y = sin(i * angle_vel_rad) * dist

    br.sendTransform((x, y, 0),
                        quaternion_from_euler(0, 0, 0),
                        rospy.Time.now(),
                        "carrot",
                        parnt_frame)
    
    i += 1 

    # rospy.loginfo(f"i={i} x={x} y={y}")

if __name__ == "__main__":
    br = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        publish_tf(br)

        rate.sleep()
