from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    for i in range(20):
        ld.add_action(
            Node(
                namespace=f'group{i:02g}',
                package='ros2_test',
                executable='exec_pubsub_nodes',
            )
        )
    ld.add_action(
        Node(
            package='ros2_test',
            executable='exec_recording_nodes_S',
        )
    )
    return ld
