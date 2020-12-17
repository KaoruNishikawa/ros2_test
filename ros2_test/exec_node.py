#!/usr/bin/env python3

import rclpy
from rclpy.executors import SingleThreadedExecutor

from .nodes.node_publish import node_publish
from .nodes.node_subscribe import node_subscribe

def main(args=None):
    rclpy.init(args=args)
    try:
        nodes = {}
        for i in range(120):
            nodes[f'pub{i:03d}'] = node_publish(
                cli_args=[
                    "--ros-args",
                    "-r", f"__node:=node_publish_{i:03d}",
                ])
            nodes[f'sub{i:03d}'] = node_subscribe(
                cli_args=[
                    "--ros-args",
                    "-r", f"__node:=node_subscribe_{i:03d}",
                ])

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

