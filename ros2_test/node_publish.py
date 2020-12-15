#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "node_publish"


class node_publish(Node):

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        self.num = int(self.declare_parameter('node_index_pub').value)
        self.pub = self.create_publisher(Float64, f"test/num", 1)
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
