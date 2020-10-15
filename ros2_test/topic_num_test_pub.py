#!/usr/bin/env python3

node_name = "topic_num_test_pub"

import rclpy
import time
from std_msgs.msg import Float64

class topic_num_test_pub(object):

    def __init__(self):
        self.node = rclpy.create_node(node_name)
        self.node.declare_parameter('node_num')
        self.num = int(self.node.get_parameter('node_num').value)
        self.num_list = [str(num) for num in range(self.num)]
        self.pub = {}
        for number in self.num_list:
            self.pub[number] = self.node.create_publisher(Float64, "/test/topic_num_"+number, 1)
        timer_period = 0.1
        self.node.create_timer(timer_period, self.pub_data)

    def pub_data(self):
        msg = Float64()
        msg.data = float(time.time())
        for number in self.num_list:
            self.pub[number].publish(msg)


def main(args=None):
    rclpy.init(args=args)
    topic_pub = topic_num_test_pub()
    rclpy.spin(topic_pub.node)

    topic_pub.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
