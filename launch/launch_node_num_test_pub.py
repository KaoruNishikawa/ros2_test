from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    nodes = []
    for i in range(5):
        nodes.append(
            Node(
                package='ros2_test',
                node_executable='node_num_pub',
                parameters=[
                    {'node_num': i}
                ]
            )
        )
    return LaunchDescription(nodes)
