from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    ld.add_action(
        Node(
            package = 'ros2_test',
            executable = 'exec_dummy_nodes',
        )
    )
    return ld
