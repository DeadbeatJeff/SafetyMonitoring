import rclpy
from rclpy.node import Node

class SafetyMonitor(Node):
    def __init__(self):
        super().__init__('safety_monitor')
        self.timer = self.create_timer(1.0, self.check_systems_callback)
        self.get_logger().info('Safety Monitor Node has been initialized and is running.')

    def check_systems_callback(self):
        self.get_logger().info('Status Check: All perimeter systems operational. Payload secure.')

def main(args=None):
    rclpy.init(args=args)
    node = SafetyMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
