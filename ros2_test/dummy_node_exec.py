#!/usr/bin/env python3

node_name = "dummy_node"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class dummy_node(Node):

    # def __init__(self, node_num=None):
    def __init__(self, parameter_overrides=None):
        super().__init__(node_name, parameter_overrides=parameter_overrides, automatically_declare_parameters_from_overrides=True)
        node_num = str(self.get_parameter('node_num').value)
        # if node_num == None:
            # node_num = str(self.declare_parameter('node_num').value)
            # node_num = str(self.get_parameter('node_num').value)
        self.pub = self.create_publisher(Float64, "/dummy_"+str(node_num), 1)
        self.create_timer(1, self.pubb)

    def pubb(self):
        msg = Float64()
        msg.data = float(time.time())
        self.pub.publish(msg)


def main(parameter_overrides=None, args=None):
    rclpy.init(args=args)
    dummy = dummy_node(parameter_overrides)
    rclpy.spin(dummy)

    dummy.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
