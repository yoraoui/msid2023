import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import ReliabilityPolicy, QoSProfile
from sensor_msgs.msg import LaserScan


class SubscriberPublisher(Node):
    def __init__(self):
        super().__init__('subscriber_publisher_tb3')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5
        self.subscriptions = self.create_subscription(LaserScan, '/scan', self.laser_callback,\
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))

        self.timer_period = 0.5
        self.laser_forward = 0.0

        self.cmd = Twist()
        self.timer = self.create_timer(self.timer_period, self.motion)


    def laser_callback(self, msg):
        self.laser_forward = msg.ranges[360]
        
    def motion(self):
        if self.laser_forward> 5:
            self.cmd.linear.x = 0.5
            self.cmd.angular.z = 0.5
        elif self.laser_forward <5 and self.laser_forward > 1:
            self.cmd.linear.x = 0.2
            self.cmd.angular.z = 0.0
        else:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.0
        self.publisher.publish(self.cmd)
                
            
              

def main(args=None):

	rclpy.init(args=args)
	subscriber_publisher = SubscriberPublisher()
	rclpy.spin(subscriber_publisher)
	subscriber_publisher.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
	main()







