#!/usr/bin/env python3

import os

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64  # noqa: F401

node_name = "cpu_checker"


class CpuChecker(Node):
    def __init__(self):
        super().__init__(node_name)
        shift = int(self.declare_parameter("shift").value)
        nodes_per_group = int(self.declare_parameter("nodes_per_group").value)
        total_pairs = int(self.declare_parameter("total_pairs").value)  # noqa: F841
        num_of_groups = int(os.environ["NUM_OF_GROUPS"])
        self.f_cpu = open(
            f"{os.environ['ROS2_TEST_SAVE_DIR']}/cpu_usage_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.csv",  # noqa: E501
            "w",
        )
        self.f_cpu.write(
            ", ".join(
                [f"CPU{i+1:02}" for i in range(len(psutil.cpu_percent(percpu=True)))]
            )
        )
        timer_period = 2
        self.create_timer(timer_period, self.checker)

    def checker(self):
        res_cpu = ", ".join(
            [str(res) for res in psutil.cpu_percent(interval=0.5, percpu=True)]
        )
        self.f_cpu.write(res_cpu + "\n")
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = CpuChecker()
        rclpy.spin(checker)
    finally:
        checker.f_cpu.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
