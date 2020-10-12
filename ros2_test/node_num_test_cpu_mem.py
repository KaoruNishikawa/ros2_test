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
            # res_mem = subprocess.check_output('top | grep cache')
            # res_cpu = subprocess.check_output('top | grep Cpu')
            command_mem_1 = 'top -b -n1'
            command_mem_2 = 'grep buff/cache'
            res = subprocess.Popen(command_mem_1.split(' '), stdout=subprocess.PIPE)
            res2 = subprocess.Popen(command_mem_2.split(" "), stdin=res.stdout, stdout=subprocess.PIPE)
            res.stdout.close()
            res_mem = res2.communicate()[0]
            # proc = subprocess.Popen(command_mem, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # res_mem, stderr_data = proc.communicate()
            # command_cpu = 'top -b | grep Cpu'
            # proc = subprocess.Popen(command_cpu, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # res_cpu, stderr_data = proc.communicate()
        except:
            res_mem = "error"
            # res_cpu = ""
        with open(f"{os.environ['HOME']}/Documents/mem_used.txt", "a") as f:
            f.write(str(res_mem)+'\n')
        # with open(f"{os.environ['HOME']}/Documents/cpu_used.txt", "a") as f:
        #     f.write(str(res_cpu)+'\n')
        # test
        self.node.get_logger().info('mem: %s, err: %s' % (res_mem, stderr_data))
        return


def main(args=None):
    rclpy.init(args=args)
    checker = cpu_mem_checker()
    rclpy.spin(checker.node)

    checker.node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
