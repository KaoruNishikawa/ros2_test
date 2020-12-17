#!/usr/bin/env python3

node_name = "cpu_checker"

import rclpy
from rclpy.node import Node
import os
import psutil
import subprocess
from std_msgs.msg import Float64

class cpu_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        # self.node = rclpy.create_node(node_name)
        timer_period = 2
        self.f_cpu = open(f"{os.environ['HOME']}/Documents/cpu_used.txt", "w")
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            # top_command = 'top -b -n1'
            # command_cpu = 'grep Cpu'
            # res_cpu1 = subprocess.Popen(top_command.split(' '), stdout=subprocess.PIPE)
            # res_cpu2 = subprocess.Popen(command_cpu.split(' '), stdin=res_cpu1.stdout, stdout=subprocess.PIPE)
            # res_cpu = res_cpu2.communicate()[0]
            res_cpu = psutil.cpu_percent(interval=0.5)
        except:
            res_cpu = ""
        self.f_cpu.write(str(res_cpu)+'\n')
        # test
        # self.node.get_logger().info('mem: %s, err: %s' % (res_mem, res_cpu))
        return


def main(args=None):
    rclpy.init(args=args)
    checker = cpu_checker()
    rclpy.spin(checker)

    checker.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
