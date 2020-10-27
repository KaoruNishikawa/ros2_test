#!/usr/bin/env python3

node_name = "mem_checker"

import rclpy
from rclpy.node import Node
import os
import subprocess
from std_msgs.msg import Float64

class mem_checker(Node):

    def __init__(self):
        super().__init__(node_name)
        # self.node = rclpy.create_node(node_name)
        timer_period = 1
        self.f_mem = open(f"{os.environ['HOME']}/Documents/mem_used.txt", "w")
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            top_command = 'top -b -n1'
            command_mem = 'grep buff/cache'
            res_mem1 = subprocess.Popen(top_command.split(' '), stdout=subprocess.PIPE)
            res_mem2 = subprocess.Popen(command_mem.split(' '), stdin=res_mem1.stdout, stdout=subprocess.PIPE)
            res_mem = res_mem2.communicate()[0]
        except:
            res_mem = ""
        self.f_mem.write(str(res_mem)+'\n')
        # test
        # self.node.get_logger().info('mem: %s, err: %s' % (res_mem, res_cpu))
        return


def main(args=None):
    rclpy.init(args=args)
    checker = mem_checker()
    rclpy.spin(checker)

    checker.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
