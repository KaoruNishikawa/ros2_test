#!/usr/bin/env python3

import rclpy
from rclpy.executors import SingleThreadedExecutor

from .node_publish import node_publish
from .node_subscribe import node_subscribe

def main(args=None):
    rclpy.init(args=args)
    try:
        nodes = {
            'pub': node_publish(),
            'sub': node_subscribe(),
        }

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
