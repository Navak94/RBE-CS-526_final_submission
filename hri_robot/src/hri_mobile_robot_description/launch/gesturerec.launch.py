from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    cmd_node = Node(
        package='hri_mobile_robot_description',
        executable='index_node',
        name='gesture_cal',
        output='screen',
        parameters=[],
    )

    index_node = Node(
        package='hri_mobile_robot_description',
        executable='cmd_node',
        name='cmd_vel_publisher_node',
        output='screen',
        parameters=[],
    )

    return LaunchDescription([
        cmd_node,
        index_node,
    ])
