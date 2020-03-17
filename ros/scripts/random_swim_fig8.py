#!/usr/bin/env python

import rospy
from math import pi
from random import randint
from random import random

from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

class ControlTurtlesim():
    

    def __init__(self):
        rospy.init_node('ControlTurtlesim', anonymous=False)
        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")
        rospy.on_shutdown(self.shutdown)

        teleport_absolute = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        teleport_absolute(randint(1,10), randint(1,10), 6.28*random())

        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=100)
        rate = rospy.Rate(100);
        rospy.loginfo("Set rate 100Hz")

        lin=randint(1,4)
        ang=randint(1,6)
        
        move_cmd = Twist()
        move_cmd.linear.x = lin
        move_cmd.angular.z = ang

        T=(2*pi)/ang
        t=0

        while not rospy.is_shutdown():
            t+=0.01
            if(t>=T):
                move_cmd.angular.z = -move_cmd.angular.z
                t=0
            self.cmd_vel.publish(move_cmd)
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
