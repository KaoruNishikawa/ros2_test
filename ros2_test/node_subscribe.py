#!/usr/bin/env python3

import os
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "node_subscribe"


class node_subscribe(Node):

    def __init__(self):
        super().__init__(node_name)
        self.num = self.declare_parameter('node_num').value
        self.f = open(f'{os.environ['HOME']}/Documents/delay_num_{self.num}.txt', "w")
        sub = self.create_subscription(Float64, "test", self.callback, 1)

    def callback(self, data):
        curr_time = float(time.time())
        sent_time = float(data.data)
        delta = curr_time - sent_time
        self.write(str(delta) + '\n')


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
