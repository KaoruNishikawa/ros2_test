from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_test',
            node_executable='node_num_pub',
            parameters=[
                {'node_num': 1},
            ]
        ),
    ])