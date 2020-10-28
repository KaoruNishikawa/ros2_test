#!/usr/bin/env python3

node_name = "net_checker"

import rclpy
from rclpy.node import Node
import os
import psutil
import subprocess
from std_msgs.msg import Float64

class net_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        timer_period = 2
        self.f_net = open(f"{os.environ['HOME']}/Documents/net_count.txt", "w")
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_net = psutil.virtual_memory()
        except:
            res_net = ""
        self.f_net.write(str(res_mem)+'\n')
        return


def main(args=None):
    rclpy.init(args=args)
    checker = net_checker()
    rclpy.spin(checker)

    checker.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
