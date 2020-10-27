#!/usr/bin/env python3

node_name = "dummy_node"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class dummy_node(Node):

    def __init__(self):
        super().__init__(node_name)
        # self.node = rclpy.create_node(node_name)
        self.declare_parameter('node_num')
        self.num = str(self.get_parameter('node_num').value)
        
def main(args=None):
    rclpy.init(args=args)
    dummy = dummy_node()
    rclpy.spin(dummy)

    dummy.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
