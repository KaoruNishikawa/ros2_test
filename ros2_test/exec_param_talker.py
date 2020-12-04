#!/usr/bin/env python3

from ros2_test.talker_exec import talker_exec

import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.parameter import Parameter


def main(args=None):
    rclpy.init(args=args)
    try:
        # talker = talker_exec(
        #         parameter_overrides=[
        #             Parameter("node_num", value=22),
        #         ]
        #     )
        talker = talker_exec(
                cli_args=[
                    "--ros-args",
                    "-r", "__node:=kore",
                    "-r", "__ns:=/doko",
                    "-p", "node_num:=39",
                ]
            )

        executor = SingleThreadedExecutor()
        executor.add_node(talker)

        try:
            executor.spin()
        finally:
            executor.shutdown()
            talker.destroy_node()
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
