#!/usr/bin/env python3

node_name = "dummy_node"

import rclpy
import time
from std_msgs.msg import Float64

class dummy_node(object):

    def __init__(self):
        self.node = rclpy.create_node(node_name)
        self.node.declare_parameter('node_num')
        self.num = str(self.node.get_parameter('node_num').value)
        
def main(args=None):
    rclpy.init(args=args)
    dummy = dummy_node()
    rclpy.spin(dummy.node)

    dummy.node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
