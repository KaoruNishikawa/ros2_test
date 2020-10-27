#!/usr/bin/env python3

node_name = "topic_num_test_sub"

import rclpy
import time
from std_msgs.msg import Float64

class topic_num_test_sub(object):

    def __init__(self):
        self.node = rclpy.create_node(node_name)
        self.node.declare_parameter('node_num')
        self.num = int(self.node.get_parameter('node_num').value)
        self.num_list = [str(num) for num in range(self.num)]
        qos = rclpy.qos.QoSProfile(depth=1)
        sub = {}
        for number in self.num_list:
            sub[number] = self.node.create_subscription(Float64, "/test/topic_num_"+number, self.callback, qos)
        
    def callback(self, timer):
        curr_time = float(time.time())
        send_time = float(timer.data)
        delta = curr_time - send_time


def main(args=None):
    rclpy.init(args=args)
    topic_sub = topic_num_test_sub()
    rclpy.spin(topic_sub.node)

    topic_sub.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
