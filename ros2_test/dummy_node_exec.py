#!/usr/bin/env python3

node_name = "dummy_node"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class dummy_node(Node):

    def __init__(self, node_num=None):
        super().__init__(node_name)
        if node_num == None:
            node_num = str(self.declare_parameter('node_num').value)
        # self.node = rclpy.create_node(node_name)


def main(args=None):
    rclpy.init(args=args)
    dummy = dummy_node()
    rclpy.spin(dummy)

    dummy.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
