#!/usr/bin/env python3

node_name = "temp_checker"

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class temp_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        timer_period = 2
        self.f_temp = open(f"{os.environ['HOME']}/Documents/cpu_temp.txt", "w")
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            res_temp = psutil.sensors_temperatures()
            res_temp = str(res_temp["coretemp"])
            res_temp = re.sub(r'[\(\)\[,\]]', '', res_temp)
            res_temp = re.sub(r'shwtemp', '\n', res_temp).split('\n')[1:]  # first elem is empty
        except:
            res_temp = []
        for temp in res_temp:
            self.f_temp.write(str(temp)+'\n')
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = temp_checker()
        rclpy.spin(checker)
    finally:
        checker.f_temp.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
