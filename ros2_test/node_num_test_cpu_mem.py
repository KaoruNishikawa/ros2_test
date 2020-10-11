#!/usr/bin/env python3

node_name = "cpu_mem_checker"

import rclpy
import os
import subprocess
from std_msgs.msg import Float64

class cpu_mem_checker(object):

    def __init__(self):
        self.node = rclpy.create_node(node_name)
        timer_period = 1
        self.node.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_mem = subprocess.check_output('top | grep cache')
            res_cpu = subprocess.check_output('top | grep Cpu')
        except:
            res_mem = None
            res_cpu = None
        with open(f"{os.environ['HOME']}/Documents/mem_used.txt", "a") as f:
            f.write(res_mem)
        with open(f"{os.environ['HOME']}/Documents/cpu_used.txt", "a") as f:
            f.write(res_cpu)
        return


def main(args=None):
    rclpy.init(args=args)
    checker = cpu_mem_checker()
    rclpy.spin(checker.node)

    checker.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
