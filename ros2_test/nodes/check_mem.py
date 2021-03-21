#!/usr/bin/env python3

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64  # noqa: F401

node_name = "mem_checker"


class MemChecker(Node):
    def __init__(self):
        super().__init__(node_name)
        shift = int(self.declare_parameter("shift").value)
        nodes_per_group = int(self.declare_parameter("nodes_per_group").value)
        total_pairs = int(self.declare_parameter("total_pairs").value)  # noqa: F841
        num_of_groups = int(os.environ["NUM_OF_GROUPS"])
        self.f_mem = open(
            f"{os.environ['ROS2_TEST_SAVE_DIR']}/mem_usage_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.csv",  # noqa: E501
            "w",
        )
        self.f_mem.write(", ".join(psutil.virtual_memory()._fields) + "\n")
        timer_period = 2
        self.create_timer(timer_period, self.checker)

    def checker(self):
        res_mem = ", ".join(
            [
                re.sub(r".*?=([\d.]*).*?$", r"\1", elem)
                for elem in psutil.virtual_memory().__repr__().split(",")
            ]
        )
        self.f_mem.write(res_mem + "\n")
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = MemChecker()
        rclpy.spin(checker)
    finally:
        checker.f_mem.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
