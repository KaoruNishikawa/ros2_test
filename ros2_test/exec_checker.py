#!/usr/bin/env python3

import time

import rclpy
from rclpy.executors import MultiThreadedExecutor

from .nodes.check_cpu import cpu_checker
from .nodes.check_mem import mem_checker
from .nodes.check_net import net_checker
from .nodes.check_temp import temp_checker
from .nodes.node_publish import node_publish
from .nodes.node_subscribe_rec import node_subscribe_rec

def main(args=None):
    rclpy.init(args=args)
    # time.sleep(15)  # wait for start of other nodes
    try:
        nodes = {
            'cpu': cpu_checker(),
            'mem': mem_checker(),
            'net': net_checker(),
            'temp': temp_checker(),
            'pub': node_publish(),
            'sub': node_subscribe_rec(),
        }

        executor = MultiThreadedExecutor()

        [executor.add_node(node) for node in nodes.values()]

        try:
            executor.spin()
        finally:
            executor.shutdown()
            [node.destroy_node() for node in nodes.values()]
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
