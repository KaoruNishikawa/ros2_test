#!/usr/bin/env python3

node_name = "mem_checker"

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class mem_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        timer_period = 2
        self.f_mem = open(f"{os.environ['HOME']}/Documents/mem_used.txt", "w")
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
