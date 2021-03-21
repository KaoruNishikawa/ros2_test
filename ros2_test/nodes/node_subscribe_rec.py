#!/usr/bin/env python3

import os
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "node_subscribe"


class NodeSubscribeRec(Node):

    NUM = 0

    def __new__(cls, **kwargs):
        cls.NUM += 1
        return super().__new__(cls)

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        self.group_srec = int(self.declare_parameter("group_srec").value)
        self.group_srec += 900
        shift = int(self.declare_parameter("shift").value)
        nodes_per_group = int(self.declare_parameter("nodes_per_group").value)
        total_pairs = int(self.declare_parameter("total_pairs").value)  # noqa: F841
        num_of_groups = int(os.environ["NUM_OF_GROUPS"])
        self.f = open(
            f"{os.environ['ROS2_TEST_SAVE_DIR']}/delay_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.csv",  # noqa: E501
            "w",
        )
        sub = self.create_subscription(  # noqa: F841
            Float64, f"/test/no{self.group_srec}", self.callback, 1
        )

    def callback(self, data):
        curr_time = float(time.time())
        sent_time = float(data.data)
        delta = curr_time - sent_time
        self.f.write(str(delta) + "\n")


def main(args=None):
    rclpy.init(args=args)
    try:
        node = NodeSubscribeRec()
        rclpy.spin(node)
    finally:
        node.f.close()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
