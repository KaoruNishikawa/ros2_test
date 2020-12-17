#!/usr/bin/env python3

node_name = "dummy_node"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class dummy_node(Node):

    def __init__(self, node_name_=None, parameter=None):
        if node_name_ is not None:
            node_name = node_name_
        super().__init__(node_name, parameter_overrides=parameter, automatically_declare_parameters_from_overrides=True)
        node_num = str(self.get_parameter('node_num').value)
        # self.pub = self.create_publisher(Float64, "/dummy_"+str(node_num), 1)
        # self.create_timer(1, self.pubb)

    # def pubb(self):
    #     msg = Float64()
    #     msg.data = float(time.time())
    #     self.pub.publish(msg)


def main(node_name_=None, parameter=None, args=None):
    try:
        rclpy.init(args=args)
        node = dummy_node(node_name_, parameter)
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
