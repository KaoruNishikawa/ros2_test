#!/usr/bin/env python3

node_name = "exec_recording"

from ros2_test.node_num_test_cpu import cpu_checker
from ros2_test.node_num_test_mem import mem_checker
from ros2_test.node_num_test_net import net_checker
from ros2_test.node_num_test_pub import node_num_test_pub
from ros2_test.node_num_test_sub_m import node_num_test_sub
import rclpy
from rclpy.executors import MultiThreadedExecutor

def main(args=None):
    rclpy.init(args=args)
    try:
        cpu_ = cpu_checker()
        mem_ = mem_checker()
        net_ = net_checker()
        pub = node_num_test_pub()
        sub = node_num_test_sub()

        executor = MultiThreadedExecutor()

        executor.add_node(cpu_)
        executor.add_node(mem_)
        executor.add_node(net_)
        executor.add_node(pub)
        executor.add_node(sub)

        try:
            executor.spin()
        finally:
            executor.shutdown()
            cpu_.destroy_node()
            mem_.destroy_node()
            net_.destroy_node()
            pub.destroy_node()
            sub.destroy_node()
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()