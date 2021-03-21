#!/usr/bin/env python3

import os
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String

node_name = "node_subscribe"


class NodeSubscribe(Node):

    NUM = 0

    def __new__(cls, **kwargs):
        cls.NUM += 1
        # cls.node_name = f"{node_name}_{cls.NUM:03d}"
        return super().__new__(cls)

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        self.group = int(self.declare_parameter("group").value)
        nodes_per_group = int(self.declare_parameter("nodes_per_group").value)
        total_pairs = int(self.declare_parameter("total_pairs").value)
        shift = int(self.declare_parameter("shift").value)
        self.num = (self.NUM + self.group * nodes_per_group + shift) % total_pairs
        sub = self.create_subscription(
            Float64, f"/test/no{self.num:03d}", self.callback, 1
        )
        if self.group < 90:
            self.create_subscription(
                String, f"/test/data_{self.num:03d}", self.str_callback, 1
            )

    def callback(self, data):
        curr_time = float(time.time())
        sent_time = float(data.data)
        delta = curr_time - sent_time

    def str_callback(self, data):
        length = len(str(data))


def main(args=None):
    rclpy.init(args=args)
    try:
        node = NodeSubscribe()
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
