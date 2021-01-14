from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    ld.add_action(
        Node(
            package='ros2_test',
            executable='exec_remap_test',
            parameters=[
                {'number': 999},
            ],
            remappings=[
                ('topic_name', 'remapped'),
                ('/node_999_1', '/NNN'),
            ],
            namespace='/test',
        )
    )