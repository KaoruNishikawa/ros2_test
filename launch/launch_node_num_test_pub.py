from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(num):
    return LaunchDescription([
        Node(
            package='ros2_test',
            node_executable='node_num_pub',
            parameters=[
                {'node_num': num},
            ]
        ),
    ])

if __name__ == '__main__':
    for i in range(5):
        generate_launch_description(i)
