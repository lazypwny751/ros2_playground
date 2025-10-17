import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PongNode(Node):
    def __init__(self):
        super().__init__('pong_node')
        self.ping_sub = self.create_subscription(String, 'ping', self.ping_callback, 10)
        self.pong_pub = self.create_publisher(String, 'pong', 10)

    def ping_callback(self, msg):
        self.get_logger().info(f'Receive: {msg.data}')
        reply = String()
        reply.data = f'Pong receive: {msg.data}'
        self.pong_pub.publish(reply)
        self.get_logger().info(f'Resend: {reply.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PongNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
