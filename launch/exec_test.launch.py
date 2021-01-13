from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    shift = 1
    total_pairs = 120
    nodes_per_group = 20
    num_of_groups = int(total_pairs / nodes_per_group)

    for i in range(num_of_groups):
        ld.add_action(
            Node(
                package="ros2_test",
                executable="exec_node",
                parameters=[
                    {"nodes_per_group": nodes_per_group},
                    {'group': i},
                    {'shift': shift},
                    {'total_pairs': total_pairs},
                ],
                namespace=f'/group{i:03d}',
            )
        )
    ld.add_action(
        Node(
            package="ros2_test",
            executable="exec_checker",
            parameters=[
                {'nodes_per_group': nodes_per_group},
                {'group': 99},
                {'group_srec': 99},
                {'shift': shift},
                {'total_pairs': total_pairs},
            ],
        )
    )
    return ld
