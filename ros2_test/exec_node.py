#!/usr/bin/env python3

import os
import time

import rclpy
from rclpy.executors import MultiThreadedExecutor

from .nodes.node_publish import NodePublish
from .nodes.node_subscribe import NodeSubscribe

def main(args=None):

    time.sleep(1)  # to measure the load on instantiation
    rclpy.init(args=args)
    try:
        nodes = {}
        for i in range(int(os.environ["ROS2_TEST_NUM_PER_GROUP"])):
            nodes[f'pub{i:03d}'] = NodePublish(
                cli_args=[
                    "--ros-args",
                    "-r", f"__node:=node_publish_{i:03d}",
                ])
            nodes[f'sub{i:03d}'] = NodeSubscribe(
                cli_args=[
                    "--ros-args",
                    "-r", f"__node:=node_subscribe_{i:03d}",
                ])

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

