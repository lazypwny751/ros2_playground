import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PingNode(Node):
    def __init__(self):
        super().__init__('ping_node')
        self.ping_pub = self.create_publisher(String, 'ping', 10)
        self.pong_sub = self.create_subscription(String, 'pong', self.pong_callback, 10)
        self.i = 0
        self.create_timer(1.0, self.send_ping)

    def send_ping(self):
        msg = String()
        msg.data = f'Ping {self.i}'
        self.get_logger().info(f'Send: {msg.data}')
        self.ping_pub.publish(msg)
        self.i += 1

    def pong_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
