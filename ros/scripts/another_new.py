#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class ControlTurtlesim():

    def __init__(self):
        rospy.init_node('ControlTurtlesim', anonymous=False)
        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=100)
        rate = rospy.Rate(100);
        rospy.loginfo("Set rate 100Hz")

        move_cmd = Twist()
        move_cmd.linear.x = 0
        move_cmd.angular.z = 0

        t=0
        key=1

        while not rospy.is_shutdown():
            t+=0.01

            if(key==1):
                t=0
                key=0

            if(t<=2.5):
                move_cmd.linear.x = 0
                move_cmd.angular.z = -1
                self.cmd_vel.publish(move_cmd)

            elif(t<=4.5):
                move_cmd.linear.x = 1
                move_cmd.angular.z = 0
                self.cmd_vel.publish(move_cmd)

            elif(t<=7):
                move_cmd.linear.x = 0
                move_cmd.angular.z = 1
                self.cmd_vel.publish(move_cmd)

            elif(t<=9):
                move_cmd.linear.x = 1
                move_cmd.angular.z = 0
                self.cmd_vel.publish(move_cmd)

            elif(t<=11.5):
                move_cmd.linear.x = 0
                move_cmd.angular.z = 1
                self.cmd_vel.publish(move_cmd)

            elif(t<=13.5):
                move_cmd.linear.x = 1
                move_cmd.angular.z = 0
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
