#!/usr/bin/env python3

import os
import re

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64  # noqa: F401

node_name = "temp_checker"


class TempChecker(Node):
    def __init__(self):
        super().__init__(node_name)
        shift = int(self.declare_parameter("shift").value)
        nodes_per_group = int(self.declare_parameter("nodes_per_group").value)
        total_pairs = int(self.declare_parameter("total_pairs").value)  # noqa: F841
        num_of_groups = int(os.environ["NUM_OF_GROUPS"])
        self.f_temp = open(
            f"{os.environ['ROS2_TEST_SAVE_DIR']}/cpu_temp_n{nodes_per_group:03d}x{num_of_groups:03d}g_s{shift:02d}.csv",  # noqa: E501
            "w",
        )
        self.f_temp.write(
            ",".join(psutil.sensors_temperatures()["coretemp"][0]._fields) + "\n"
        )
        timer_period = 2
        self.create_timer(timer_period, self.checker)

    def checker(self):
        try:
            for cpu in psutil.sensors_temperatures()["coretemp"]:
                self.f_temp.write(
                    ",".join(
                        [
                            re.sub(
                                r".*?=([\'\"][a-zA-Z \d]*[\'\"]|[\d.]*).*?$",
                                r"\1",
                                elem,
                            )
                            for elem in cpu.__repr__().split(",")
                        ]
                    )
                    + "\n"
                )
        except AttributeError:  # implementation of this function is OS dependent
            pass
        return


def main(args=None):
    rclpy.init(args=args)
    try:
        checker = TempChecker()
        rclpy.spin(checker)
    finally:
        checker.f_temp.close()
        checker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
