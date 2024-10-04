from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hon_bk2_temperature',
            executable='temperature_generator',
            output='screen'
        ),
        Node(
            package='hon_bk2_temperature',
            executable='alert_node',
            output='screen'
        ),
    ])