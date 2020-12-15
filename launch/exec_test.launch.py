from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    for i in range(1):
        ld.add_action(
            Node(
                package="ros2_test",
                executable="exec_node",
                parameters=[
                    {"node_index_pub": i},
                    {"node_index_sub": i},
                ],
                remappings=[
                    ("__ns", f"/group{i:03d}"),
                ],
            )
        )
    ld.add_action(
        Node(
            package="ros2_test",
            executable="exec_checker",
            parameters=[
                {"node_num": 999},
                {"node_index_pub": 999},
                {"node_index_sub": 999},
            ],
            remappings=[
                ("test/num", "test/no999"),
            ],
        )
    )
    return ld
