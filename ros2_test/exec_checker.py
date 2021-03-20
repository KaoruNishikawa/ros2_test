#!/usr/bin/env python3

import time

import rclpy
from rclpy.executors import MultiThreadedExecutor

from .nodes.check_cpu import CpuChecker
from .nodes.check_mem import MemChecker
from .nodes.check_net import NetChecker
from .nodes.check_temp import TempChecker
from .nodes.node_publish import NodePublish
from .nodes.node_subscribe_rec import NodeSubscribeRec

def main(args=None):
    rclpy.init(args=args)
    try:
        nodes = {
            'cpu': CpuChecker(),
            'mem': MemChecker(),
            'net': NetChecker(),
            'temp': TempChecker(),
            'pub': NodePublish(),
            'sub': NodeSubscribeRec(),
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
