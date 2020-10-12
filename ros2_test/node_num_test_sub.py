#!/usr/bin/env python3

node_name = "delay_test_sub"

import rclpy
import time
import os
from std_msgs.msg import Float64

class node_num_test_sub(object):
    
    def __init__(self):
        self.node = rclpy.create_node(node_name)
        self.node.declare_parameter('node_num')
        self.num = str(self.node.get_parameter('node_num').value)
        subscriber = self.node.create_subscription(Float64, "/test/node_num_"+self.num, self.sub_callback, 1)

    def sub_callback(self, timer):
        current_time = float(time.time())
        send_time = float(timer.data)
        delta = current_time - send_time
        with open(f"{os.environ['HOME']}/Documents/node_num_test/test_node_num_{self.num}.txt", "a") as f:
            f.write(str(delta)+'\n')


def main(args=None):
    rclpy.init(args=args)
    subscriber = node_num_test_sub()
    rclpy.spin(subscriber.node)

    subscriber.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

