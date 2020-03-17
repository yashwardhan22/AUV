#!/usr/bin/env python

import rospy
from math import pi

from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative

class ControlTurtlesim():
    

    def __init__(self):
        rospy.init_node('ControlTurtlesim', anonymous=False)
        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")
        rospy.on_shutdown(self.shutdown)

        tel_abs = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        tel_rel = rospy.ServiceProxy('/turtle1/teleport_relative',TeleportRelative)

        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(1);
        rospy.loginfo("Set rate 1Hz")
        
        tel_abs(5, 9, -2*pi/3)
        move_cmd = Twist()

        rospy.loginfo(move_cmd)

        move_cmd.linear.x = 3
        self.cmd_vel.publish(move_cmd)
        rate.sleep()
        rospy.loginfo(move_cmd)

#        move_cmd.angular.z = 0
        
#        while not rospy.is_shutdown():
#            self.cmd_vel.publish(move_cmd)
            

    def shutdown(self):
        rospy.loginfo("Stopping the turtle")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        ControlTurtlesim()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
