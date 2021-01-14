#!/usr/bin/env python3

import rclpy
from rclpy.executors import SingleThreadedExecutor

from .nodes.remap_test import RemapTest


def main(args=args):
    rclpy.init(args=args)
    try:
        nodes = {}
        for i in range(5):
            nodes[f'pub{i}'] = RemapTest()

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
