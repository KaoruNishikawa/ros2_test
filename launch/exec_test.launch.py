from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    # ld.add_action(
    #     Node(
    #         package="ros2_test",
    #         executable="exec_node",
    #         parameters=[
    #             {"node_num":1},
    #         ],
    #     )
    # )
    ld.add_action(
        Node(
            package="ros2_test",
            executable="exec_checker",
            parameters=[
                {"node_num": 999},
            ],
            remappings=[
                ("test", "testing"),
            ],
        )
    )
    return ld
