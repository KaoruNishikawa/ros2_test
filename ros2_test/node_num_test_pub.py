#!/usr/bin/env python3

node_name = "delay_test_pub"

import rclpy
import time
from std_msgs.msg import Float64

class communication_test_pub(object):

    def __init__(self):
        self.node = rclpy.create_node(node_name)
        self.node.declare_parameter('node_num')
        self.num = str(self.node.get_parameter('node_num').value)
        self.my_pub = self.node.create_publisher(Float64, "/test/node_num_"+self.num, 1)
        timer_period = 0.1
        self.node.create_timer(timer_period, self.my_publisher)

    def my_publisher(self):
        msg = Float64()
        msg.data = float(time.time())
        self.my_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    pub = communication_test_pub()
    rclpy.spin(pub.node)

    pub.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

