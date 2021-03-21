#!/usr/bin/env python3

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64  # noqa: F401

node_name = "net_checker"


class NetChecker(Node):
    def __init__(self):
        super().__init__(node_name)
        shift = int(self.declare_parameter("shift").value)
        nodes_per_group = int(self.declare_parameter("nodes_per_group").value)
        total_pairs = int(self.declare_parameter("total_pairs").value)  # noqa: F841
        num_of_groups = int(os.environ["NUM_OF_GROUPS"])
        self.f_net = open(
            f"{os.environ['ROS2_TEST_SAVE_DIR']}/net_count_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.csv",  # noqa: E501
            "w",
        )
        self.f_net.write(", ".join(psutil.net_io_counters()._fields) + "\n")
        timer_period = 2
        self.create_timer(timer_period, self.checker)

    def checker(self):
        res_net = ", ".join(
            [
                re.sub(r".*?=([\d.]*).*?$", r"\1", elem)
                for elem in psutil.net_io_counters().__repr__().split(",")
            ]
        )
        self.f_net.write(str(res_net) + "\n")
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = NetChecker()
        rclpy.spin(checker)
    finally:
        checker.f_net.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
