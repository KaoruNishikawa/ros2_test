from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    nodes = []
    for i in range(5):
        nodes.append(
            Node(
                package='ros2_test',
                node_executable='topic_num_pub',
                parameters=[
                    {'node_num': i}
                ]
            )
        )
        nodes.append(
            Node(
                package='ros2_test',
                node_executable='topic_num_sub',
                parameters=[
                    {'node_num': i}
                ]
            )
        )
    nodes.append(
        Node(
            package='ros2_test',
            node_executable='mem_cpu_checker',
        )
    )
    nodes.append(
        Node(
            packages='ros2_test',
            node_executable='node_num_pub',
            parameter=[
                {'node_num': 0}
            ]
        )
    )
    nodes.append(
        Node(
            package='ros2_test',
            node_executable='node_num_sub_m',
            parameter=[
                {'node_num': 0}
            ]
        )
    )
    return LaunchDescription(nodes)
    