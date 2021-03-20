#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String

node_name = "node_publish"


class NodePublish(Node):

    NUM = 0

    def __new__(cls, **kwargs):
        cls.NUM += 1
        return super().__new__(cls)

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        self.group = int(self.declare_parameter('group').value)
        nodes_per_group = int(self.declare_parameter('nodes_per_group').value)
        total_pairs = int(self.declare_parameter('total_pairs').value)
        if self.group < 90:
            self.num = (self.NUM + self.group * nodes_per_group) % total_pairs
            self.data_pub = self.create_publisher(String, f"/test/data_{self.num:03d}", 1)
        else:
            self.num = 900 + self.group
        self.pub = self.create_publisher(Float64, f"/test/no{self.num:03d}", 1)
        timer_period = 0.1
        self.create_timer(timer_period, self.talker)

    def talker(self):
        msg = Float64()
        msg.data = float(time.time())
        self.pub.publish(msg)
        if self.num < 90:
            data = String()
            data.data = 'a' * 1000
            self.data_pub.publish(data)


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
