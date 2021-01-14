#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class RemapTest(Node):
    NUM = 0

    def __new__(cls):
        cls.NUM += 1
        return super(RemapTest, cls).__new__(cls)

    def __init__(self):
        super().__init__('remap_test')
        num = int(self.declare_parameter('number').value)
        self.publisher = self.create_publisher(Float64, f'node_{num}_{self.NUM}', 1)
        self.publisher2 = self.create_publisher(Float64, 'topic_name', 1)
        self.create_timer(1, self.talker)

    def talker(self):
        msg = Float64()
        msg.data = time.time()
        self.publisher.publish(msg)
        msg2 = Float64
        msg2.data = 2
        self.publisher2.publish(msg2)


def main(args=None):
    rclpy.init(args=args)
    try:
        node = RemapTest()
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
