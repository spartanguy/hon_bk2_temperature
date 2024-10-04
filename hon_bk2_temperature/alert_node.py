import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Alertnode(Node):
    def __init__(self):
        super.__init__('alert_node')
        self.subscription = self.create_subscription(Float32, 'temperature', self.check_temperature, 10)
        self.publisher = self.create_publisher(str,'temperature_alert', 10)

    def check_temperature(self,msg):
        if (msg.data > 25.0):
            alert_msg = str()
            alert_msg.data = "Hőmérséklet túl magas!"
            self.publisher.publish(alert_msg)
            self.get_logger().info('Alert: A hőmérséklet túl magas!!')

def main(args=None):
    rclpy.init(args=args)
    node = Alertnode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()  