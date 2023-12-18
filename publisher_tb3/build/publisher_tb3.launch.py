from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
			Node(
				package ='publisher_tb3',
				executable = 'publisher_tb3',
				output = 'screen'
				),
		])