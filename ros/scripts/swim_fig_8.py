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

        teleport_absolute = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        teleport_absolute(5, 5, 0)
        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        rate = rospy.Rate(100);
        rospy.loginfo("Set rate 10Hz")
        lin=input("Enter linear velocity:")
        ang=input("Enter angular veocity:")
        
        move_cmd = Twist()
        move_cmd.linear.x = int(lin)
        move_cmd.angular.z = int(ang)

        T=(2*pi)/int(ang)
        t=0

        while not rospy.is_shutdown():
            t+=0.01
            if(t>T):
                move_cmd.angular.z = -move_cmd.angular.z
                t=0
            self.cmd_vel.publish(move_cmd)
            rospy.loginfo(t)
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
