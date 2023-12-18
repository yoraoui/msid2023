import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist



class simplePublisher(Node):
	def __init__(self):
		super().__init__('publisher_tb3')
		self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def timer_callback(self):
		msg = Twist()
		msg.linear.x =0.5
		msg.angular.z=0.0
		self.publisher.publish(msg)
		self.get_logger().info('Publishing:"%s"'%msg.linear.x)



def main(args=None):

	rclpy.init(args=args)
	simple_publisher = simplePublisher()
	rclpy.spin(simple_publisher)
	simple_publisher.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
	main()







