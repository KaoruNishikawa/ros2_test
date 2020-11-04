from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    ld.add_action(
        Node(
            package='ros2_test',
            executable='topic_num_pub',
            parameters=[
                {'topic_num': 400}
            ]
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='topic_num_sub',
            parameters=[
                {'topic_num': 400}
            ]
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='mem_checker',
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='cpu_checker',
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='net_checker',
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='node_num_pub',
            parameters=[
                {'node_num': 0}
            ]
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='node_num_sub_m',
            parameters=[
                {'node_num': 0}
            ]
        )
    )
    return ld
    
