#!/usr/bin/env python3

import os

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

node_name = "cpu_checker"


class cpu_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        timer_period = 2
        self.num = int(self.declare_parameter('node_num').value)
        self.f_cpu = open(f"{os.environ['HOME']}/Documents/cpu_used_{self.num:03d}.txt", "w")
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
