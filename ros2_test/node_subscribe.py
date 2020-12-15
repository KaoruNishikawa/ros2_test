#!/usr/bin/env python3

import os
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "node_subscribe"


class node_subscribe(Node):

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        self.num = int(self.declare_parameter('node_index_sub').value)
        self.f = open(f"{os.environ['HOME']}/Documents/delay_{self.num:03d}.txt", "w")
        sub = self.create_subscription(Float64, "test/num", self.callback, 1)

    def callback(self, data):
        curr_time = float(time.time())
        sent_time = float(data.data)
        delta = curr_time - sent_time
        self.f.write(str(delta) + '\n')


def main(args=None):
    rclpy.init(args=args)
    try:
        node = node_subscribe()
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
