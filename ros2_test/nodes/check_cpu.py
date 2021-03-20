#!/usr/bin/env python3

import os

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "cpu_checker"


class CpuChecker(Node):

    def __init__(self):
        super().__init__(node_name)
        shift = int(self.declare_parameter('shift').value)
        nodes_per_group = int(self.declare_parameter('nodes_per_group').value)
        total_pairs = int(self.declare_parameter('total_pairs').value)
        num_of_groups = int(os.environ['NUM_OF_GROUPS'])
        self.f_cpu = open(
            f"{os.environ['ROS2_TEST_SAVE_DIR']}/cpu_usage_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.txt",  # noqa: E501
            "w"
        )
        timer_period = 2
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_cpu = psutil.cpu_percent(interval=0.5, percpu=True)
            res_cpu = " ".join([str(res) for res in res_cpu])
        except:
            res_cpu = ""
        self.f_cpu.write(res_cpu+'\n')
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = cpu_checker()
        rclpy.spin(checker)
    finally:
        checker.f_cpu.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
