#!/usr/bin/env python

import rospy
from math import pi

from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

class ControlTurtlesim():
    

    def __init__(self):
        rospy.init_node('ControlTurtlesim', anonymous=False)
        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")
        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        rate = rospy.Rate(100);
        rospy.loginfo("Set rate 100Hz")
        
        move_cmd1 = Twist()
        move_cmd1.linear.x = 1
        move_cmd1.angular.z = 0

        move_cmd2 = Twist()
        move_cmd2.linear.x = 0
        move_cmd2.angular.z = 1

        t=0

        while not rospy.is_shutdown():
           	t+=0.01

            if(t>=2):
                move_cmd.angular.z = -move_cmd.angular.z
                t=0
            self.cmd_vel.publish(move_cmd1)
			

            rate.sleep()

    def shutdown(self):
        rospy.loginfo("Stopping the turtle")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        ControlTurtlesim()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
