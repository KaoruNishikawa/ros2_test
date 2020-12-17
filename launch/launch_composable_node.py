from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    ld = LaunchDescription()
    for i in range(1):
        ld.add_action(
            Node(
                package='ros2_test',
                executable='node_num_pub',
                parameters=[
                    {'node_num': i}
                ]
            )
        )
        ld.add_action(
            Node(
                package='ros2_test',
                executable='dummy_sub',
                parameters=[
                    {'node_num': i}
                ]
            )
        )
    recorders = ComposableNodeContainer(
            name = 'recorders_container',
            namespace = '/record',
            package = 'rclcpp_components',
            executable = 'component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package = 'ros2_test',
                    plugin = 'cpu_checker',
                    name = 'cpu_checker',
                ),
                ComposableNode(
                    package = 'ros2_test',
                    plugin = 'mem_checker',
                    name = 'mem_checker',
                ),
                ComposableNode(
                    package = 'ros2_test',
                    plugin = 'node_num_sub_m',
                    parameters = [
                        {'node_num': 0}
                    ],
                    name = 'node_num_sub_m',
                ),
            ])
    ld.add_action(recorders)
    return ld
