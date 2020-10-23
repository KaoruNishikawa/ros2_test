from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    node_num = LaunchConfiguration('node_number', default=1)
    # for i in range(int(node_num)):
    for i in range(5):
        pass
    return LaunchDescription([
        Node(
            package='ros2_test',
            executable='node_num_pub',
            parameters=[
                {'node_num': node_num}
                ]
            ),
        Node(
            package='ros2_test',
            executable='node_num_sub_m',
            parameters=[
                {'node_num': node_num}
                ]
            ),
        ])
