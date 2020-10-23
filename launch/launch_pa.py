# from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import LogInfo #, IncludeLaunchDescription, DeclareLaunchArgument
# from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration #, ThisLaunchFileDir

def generate_launch_description():
    # package_prefix = get_package_share_directory('ros2_test')
    node_num = LaunchConfiguration('node_number', default='1')
    # node_iter = range(node_num)
    str(node_num)

    return LaunchDescription([
        # DeclareLaunchArgument(
            # 'node_number',
            # default_value = '1',
            # description = 'number of nodes to launch'),
        # IncludeLaunchDescription(
            # PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/launch_ch.py']),
            # launch_arguments = {'node_number': node_num}.items()
            # ),
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
        LogInfo(msg=['type of node_num is: ', str(type(node_num))]),
        LogInfo(msg=['node_num is: ', str(node_num.variable_name)]),
        ])
