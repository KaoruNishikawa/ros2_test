from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    for i in range(5):
        ld.add_action(
            Node(
                package='ros2_test',
                executable='dummy_node',
                name='dummy_node'+str(i),
                parameters=[
                    {'node_num': i}
                ]
            )
        )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='mem_checker',
            name='mem_checker',
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='cpu_checker',
            name='cpu_checker',
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='node_num_pub',
            name='delay_pub',
            parameters=[
                {'node_num': 0}
            ]
        )
    )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='node_num_sub_m',
            name='delay_sub',
            parameters=[
                {'node_num': 0}
            ]
        )
    )
    return ld
