#!/usr/bin/env python3

node_name = "exec_dummy"

from ros2_test.dummy_node_exec import dummy_node
import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.parameter import Parameter

def main(args=None):
    rclpy.init(args=args)
    try:
        param = [[Parameter("node_num", value=f"{i:02g}")] for i in range(20)]
        nodes = [dummy_node(parameter_overrides = param[i]) for i in range(20)]

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
