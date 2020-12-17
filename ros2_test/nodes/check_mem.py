#!/usr/bin/env python3

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "mem_checker"


class mem_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        shift = int(self.declare_parameter('shift').value)
        nodes_per_group = int(self.declare_parameter('nodes_per_group').value)
        total_pairs = int(self.declare_parameter('total_pairs').value)
        num_of_groups = int(total_pairs / nodes_per_group)
        self.f_mem = open(f"{os.environ['HOME']}/Documents/mem_used_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.txt", "w")
        timer_period = 2
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_mem = str(psutil.virtual_memory())
            res_mem = re.sub(r'.*\(', '', res_mem)
            res_mem = re.sub(r'[,\)$]', '', res_mem)
        except:
            res_mem = ""
        self.f_mem.write(res_mem+'\n')
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = mem_checker()
        rclpy.spin(checker)
    finally:
        checker.f_mem.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
