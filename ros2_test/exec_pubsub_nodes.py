#!/usr/bin/env python3

node_name = "exec_pubsub"

from .nodes.talker_exec import talker_exec
from .nodes.listener_exec import listener_exec
import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.parameter import Parameter

def main(args=None):
    rclpy.init(args=args)
    try:
        param = [[Parameter("node_num", value=f"{i:02g}")] for i in range(10)]
        t_name = [f"talker_{i:02g}" for i in range(10)]
        l_name = [f"listener_{i:02g}" for i in range(10)]
        t_nodes = [talker_exec(node_name_=t_name[i], parameter=param[i]) for i in range(10)]
        l_nodes = [listener_exec(node_name_=l_name[i], parameter=param[i]) for i in range(10)]
        nodes = t_nodes + l_nodes

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
