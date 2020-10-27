#!/usr/bin/env python3

node_name = "delay_test_sub"

import rclpy
from rclpy.node import Node
import time
import os
from std_msgs.msg import Float64

class node_num_test_sub(Node):
    
    def __init__(self):
        super().__init__(node_name)
        # self.node = rclpy.create_node(node_name)
        self.declare_parameter('node_num')
        self.num = str(self.get_parameter('node_num').value)
        self.f = open(f"{os.environ['HOME']}/Documents/test_node_num_{self.num}.txt", "w")
        qos = rclpy.qos.QoSProfile(depth=1)
        subscriber = self.create_subscription(Float64, "/test/node_num_"+self.num, self.sub_callback, qos)

    def sub_callback(self, timer):
        current_time = float(time.time())
        send_time = float(timer.data)
        delta = current_time - send_time
        self.f.write(str(delta)+'\n')
        # test
        # self.node.get_logger().info('write')


def main(args=None):
    rclpy.init(args=args)
    subscriber = node_num_test_sub()
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

