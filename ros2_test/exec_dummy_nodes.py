#!/usr/bin/env python3

node_name = "exec_dummy"

from ros2_test.dummy_node_exec import dummy_node
import rclpy
from rclpy.executors import SingleThreadedExecutor

def main(args=None):
    rclpy.init(args=args)
    try:
        nodes = [dummy_node(node_num=i) for i in range(20)]

        executor = SingleThreadedExecutor()

        [executor.add_node(node) for node in nodes]

        try:
            executor.spin()
        finally:
            executor.shutdown()
            [node.shutdown() for node in nodes]
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()