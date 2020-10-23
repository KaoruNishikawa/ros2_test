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
        self.f_mem = open(f"{os.environ['HOME']}/Documents/mem_used.txt", "w")
        self.f_cpu = open(f"{os.environ['HOME']}/Documents/cpu_used.txt", "w")
        self.node.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            top_command = 'top -b -n1'
            command_mem = 'grep buff/cache'
            res_mem1 = subprocess.Popen(top_command.split(' '), stdout=subprocess.PIPE)
            res_mem2 = subprocess.Popen(command_mem.split(' '), stdin=res_mem1.stdout, stdout=subprocess.PIPE)
            res_mem = res_mem2.communicate()[0]
            command_cpu = 'grep Cpu'
            res_cpu1 = subprocess.Popen(top_command.split(' '), stdout=subprocess.PIPE)
            res_cpu2 = subprocess.Popen(command_cpu.split(' '), stdin=res_cpu1.stdout, stdout=subprocess.PIPE)
            res_cpu = res_cpu2.communicate()[0]
        except:
            res_mem = ""
            res_cpu = ""
        self.f_mem.write(str(res_mem)+'\n')
        self.f_cpu.write(str(res_cpu)+'\n')
        # test
        # self.node.get_logger().info('mem: %s, err: %s' % (res_mem, res_cpu))
        return


def main(args=None):
    rclpy.init(args=args)
    checker = cpu_mem_checker()
    rclpy.spin(checker.node)

    checker.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
