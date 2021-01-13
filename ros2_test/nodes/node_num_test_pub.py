#!/usr/bin/env python3

node_name = "delay_test_pub"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class node_num_test_pub(Node):

    def __init__(self):
        super().__init__(node_name)
        # self.node = rclpy.create_node(node_name)
        self.declare_parameter('node_num')
        self.num = str(self.get_parameter('node_num').value)
        qos = rclpy.qos.QoSProfile(depth=1)
        self.my_pub = self.create_publisher(Float64, f"test/node/{self.num}", qos)
        timer_period = 0.1
        self.create_timer(timer_period, self.my_publisher)

    def my_publisher(self):
        msg = Float64()
        msg.data = float(time.time())
        self.my_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    pub = node_num_test_pub()
    rclpy.spin(pub)

    pub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

