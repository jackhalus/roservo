#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('gripper', Int16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        servo_signal = Int16()
        servo_signal.data = int(input("input position"))
        # rospy.loginfo(servo_signal)
        pub.publish(servo_signal)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass