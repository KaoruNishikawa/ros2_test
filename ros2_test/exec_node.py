#!/usr/bin/env python3

import rclpy
from rclpy.executors import SingleThreadedExecutor

from .node_publish import node_publish
from .node_subscribe import node_subscribe

def main(args=None):
    rclpy.init(args=args)
    try:
        nodes = {}
        dev = 0
        for i in range(20):
            nodes[f'pub{i:03d}'] = node_publish(
                cli_args=[
                    "--ros-args",
                    "-r", f"test/num:=test/no{i:03d}",
                ]),
            nodes[f'sub{i:03d}'] = node_subscribe(
                cli_args=[
                    "--ros-args",
                    "-r", f"test/num:=test/no{i+dev:03d}",
                ]),

        executor = SingleThreadedExecutor()

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
