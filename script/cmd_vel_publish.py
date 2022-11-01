import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/dynamixel_workbench/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(1) # 1hz
    cnt = 0
    max_cmd = 7
    while not rospy.is_shutdown():
        msg = Twist()
        if cnt % max_cmd == 0:
            msg.linear.x = 0.04
        elif cnt % max_cmd == 1:
            msg.linear.x = -0.04
        elif cnt % max_cmd == 2:
            msg.linear.y = 0.04
        elif cnt % max_cmd == 3:
            msg.linear.y = -0.04
        elif cnt % max_cmd == 4:
            msg.angular.z = 0.3
        elif cnt % max_cmd == 5:
            msg.angular.z = -0.3
        cnt += 1
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass