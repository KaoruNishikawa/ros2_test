#!/usr/bin/env python3

node_name = "cpu_checker"

import rclpy
from rclpy.node import Node
import os
import psutil
from std_msgs.msg import Float64

class cpu_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        timer_period = 2
        self.f_cpu = open(f"{os.environ['HOME']}/Documents/cpu_used.txt", "w")
        # self.data = []
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_cpu = psutil.cpu_percent(interval=0.5, percpu=True)
        except:
            res_cpu = ""
        self.f_cpu.write(str(res_cpu)+'\n')
        # self.data.append(str(res_cpu)+'\n')
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = cpu_checker()
        rclpy.spin(checker)
    finally:
        # print(checker.data)
        # checker.f_cpu.write(str(checker.data))
        checker.f_cpu.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
