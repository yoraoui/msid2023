import  rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile


class simpleSubscriber(Node):
    def __init__(self):
        super().__init__('subscriber_pkg')
        self.subscription = self.create_subscription(LaserScan, '/scan', self.listener_callback,\
                QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard:"%s"'%str(msg))

def main(args=None):
    rclpy.init(args=args)
    simple_subscriber = simpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()

