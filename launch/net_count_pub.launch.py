from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    num_of_subs = 1

    ld.add_action(
        Node(
            package="ros2_test",
            executable="node_publish",
            parameters=[
                {"nodes_per_group": 1},
                {"group": 1},
                {"total_pairs": 1}
            ]
        )
    )
    # for i in range(num_of_subs):
    #     ld.add_action(
    #         Node(
    #             package="ros2_test",
    #             executable="node_subscribe",
    #             parameters=[
    #                 {"nodes_per_group": 1},
    #                 {'group': 1},
    #                 {'shift': 0},
    #                 {'total_pairs': 1},
    #             ],
    #         )
    #     )
    ld.add_action(
        Node(
            package="ros2_test",
            executable="exec_checker",
            parameters=[
                {'nodes_per_group': 1},
                {'group': 98},
                {'group_srec': 97},
                {'shift': 0},
                {'total_pairs': 1},
            ],
        )
    )
    return ld
