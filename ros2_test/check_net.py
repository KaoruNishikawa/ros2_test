#!/usr/bin/env python3

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "net_checker"


class net_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        timer_period = 2
        self.f_net = open(f"{os.environ['HOME']}/Documents/net_count.txt", "w")
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_net = psutil.net_io_counters()
            res_net = re.sub(r'.*?\(', '', str(res_net))
            res_net = re.sub(r'[,\)]', '', res_net)
        except:
            res_net = ""
        self.f_net.write(str(res_net)+'\n')
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = net_checker()
        rclpy.spin(checker)
    finally:
        checker.f_net.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
