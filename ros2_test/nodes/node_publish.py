#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "node_publish"


class node_publish(Node):

    NUM = 0

    def __new__(cls, **kwargs):
        cls.NUM += 1
        return super().__new__(cls)

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        self.group = int(self.declare_parameter('group').value)
        nodes_per_group = int(self.declare_parameter('nodes_per_group').value)
        total_pairs = int(self.declare_parameter('total_pairs').value)
        if not self.group == 99:
            self.num = (self.NUM + self.group * nodes_per_group) % total_pairs
        else:
            self.num = 999
        self.pub = self.create_publisher(Float64, f"/test/no{self.num:03d}", 1)
        timer_period = 0.1
        self.create_timer(timer_period, self.talker)

    def talker(self):
        msg = Float64()
        msg.data = float(time.time())
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    try:
        node = node_publish()
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
