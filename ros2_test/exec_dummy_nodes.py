#!/usr/bin/env python3

node_name = "exec_dummy"

import time

from .nodes.dummy_node_exec import dummy_node
import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.parameter import Parameter

def main(args=None):
    time.sleep(10)
    rclpy.init(args=args)
    try:
        param = [[Parameter("node_num", value=f"{i:02g}")] for i in range(20)]
        name = [f"dummy_node_{i:02g}" for i in range(20)]
        nodes = [dummy_node(node_name_=name[i], parameter=param[i]) for i in range(20)]

        executor = SingleThreadedExecutor()

        [executor.add_node(node) for node in nodes]

        try:
            executor.spin()
        finally:
            executor.shutdown()
            [node.destroy_node() for node in nodes]
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
