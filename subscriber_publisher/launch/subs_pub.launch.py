from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
            Node(
                package ='subscriber_publisher',
                executable = 'subscriber_publisher',
                output = 'screen'
                ),
        ])