#!/usr/bin/env python3

node_name = "topic_num_test_pub"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class topic_num_test_pub(Node):

    def __init__(self):
        super().__init__(node_name)
        # self.node = rclpy.create_node(node_name)
        self.declare_parameter('node_num')
        self.num = int(self.get_parameter('node_num').value)
        self.num_list = [str(num) for num in range(self.num)]
        qos = rclpy.qos.QoSProfile(depth=1)
        self.pub = {}
        for number in self.num_list:
            self.pub[number] = self.create_publisher(Float64, "/test/topic_num_"+number, qos)
        timer_period = 0.1
        self.create_timer(timer_period, self.pub_data)

    def pub_data(self):
        msg = Float64()
        msg.data = float(time.time())
        for number in self.num_list:
            self.pub[number].publish(msg)


def main(args=None):
    rclpy.init(args=args)
    topic_pub = topic_num_test_pub()
    rclpy.spin(topic_pub)

    topic_pub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
