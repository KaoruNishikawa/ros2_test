#!/usr/bin/env python3

node_name = "cpu_mem_checker"

import rclpy
import os
import subprocess
import time
from std_msgs.msg import Float64

class cpu_mem_checker(object):

    def __init__(self):
        self.node = rclpy.create_node(node_name)
        timer_period = 2
        self.node.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            command_mem_1 = 'top -b -n1'
            command_mem_2 = 'grep buff/cache'
            res1_mem = subprocess.Popen(command_mem_1.split(' '), stdout=subprocess.PIPE)
            res2_mem = subprocess.Popen(command_mem_2.split(' '), stdin=res.stdout, stdout=subprocess.PIPE)
            res_mem = res2.communicate()[0]
            # time.sleep(1)
            # command_cpu_1 = 'top -b -n1'
            # command_cpu_2 = 'grep Cpu'
            # res1_cpu = subprocess.Popen(command_cpu_1.split(' '), stdout=subprocess.PIPE)
            # res2_cpu = subprocess.Popen(command_cpu_2.split(' '), stdin=res.stdout, stdout=subprocess.PIPE)
            # res_cpu = res2.communicate()[0]
        except:
            res_mem = "error"
            # res_cpu = ""
        with open(f"{os.environ['HOME']}/Documents/mem_used.txt", "a") as f:
            f.write(str(res_mem)+'\n')
        # with open(f"{os.environ['HOME']}/Documents/cpu_used.txt", "a") as f:
        #     f.write(str(res_cpu)+'\n')
        # test
        self.node.get_logger().info('mem: %s, cpu: %s' % (res_mem, res_mem))
        return


def main(args=None):
    rclpy.init(args=args)
    checker = cpu_mem_checker()
    rclpy.spin(checker.node)

    checker.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
