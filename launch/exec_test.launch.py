import os

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    shift = int(os.environ["ROS2_TEST_SHIFT"])
    total_pairs = int(os.environ["ROS2_TEST_TOPIC_NUM"])
    nodes_per_group = int(os.environ["ROS2_TEST_NUM_PER_GROUP"])
    try:
        num_of_groups = int(total_pairs / nodes_per_group)
    except ZeroDivisionError:
        num_of_groups = 0
    os.environ['NUM_OF_GROUPS'] = str(num_of_groups)

    for i in range(num_of_groups):
        ld.add_action(
            Node(
                package="ros2_test",
                node_executable="exec_node",
                parameters=[
                    {"nodes_per_group": nodes_per_group},
                    {'group': i},
                    {'shift': shift},
                    {'total_pairs': total_pairs},
                ],
                node_namespace=f'/group{i:03d}',
                # arguments=["--nodeNum=20"],
            )
        )
    ld.add_action(
        Node(
            package="ros2_test",
            node_executable="exec_checker",
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
