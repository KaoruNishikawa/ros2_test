#!/usr/bin/env python3

node_name = "listener_exec"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class listener_exec(Node):

    def __init__(self, node_name_=None, parameter=None):
        if node_name_ is not None:
            node_name = node_name_
        super().__init__(node_name, parameter_overrides=parameter, automatically_declare_parameters_from_overrides=True)
        node_num = str(self.get_parameter('node_num').value)
        # self.pub = self.create_publisher(Float64, "/dummy_"+str(node_num), 1)
        # self.create_timer(1, self.pubb)
        sub = self.create_subscription(Float64, "exec_pubsub_"+str(node_num), self.callback, 1)

    def callback(self, timer):
        curr_time = time.time()
        sent_time = timer.data
        delta = float(curr_time) - float(sent_time)


def main(node_name_=None, parameter=None, args=None):
    try:
        rclpy.init(args=args)
        node = listener_exec(node_name_, parameter)
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
