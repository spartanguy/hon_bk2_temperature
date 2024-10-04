import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class AlertNode(Node):

    def __init__(self):
        super().__init__('alert_node')
        self.subscription = self.create_subscription(Float32, 'temperature', self.check_temperature, 10)
        self.publisher_ = self.create_publisher(String, 'temperature_alert', 10)
        self.get_logger().info(f'Élek virulok')

    def check_temperature(self, msg):
        if msg.data > 25.0:
            alert_msg = String()
            alert_msg.data = "Hőmérséklet túl magas!"
            self.publisher_.publish(alert_msg)
            self.get_logger().info('Alert: Hőmérséklet túl magas!')

def main(args=None):
    rclpy.init(args=args)
    node = AlertNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()