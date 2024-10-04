import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureGenerator(Node):

    def __init__(self):
        super().__init__('temperature_generator')
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)

    def publish_temperature(self):
        msg = Float32()
        msg.data = random.uniform(15.0, 30.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing temperature: {msg.data:.2f} °C')


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()