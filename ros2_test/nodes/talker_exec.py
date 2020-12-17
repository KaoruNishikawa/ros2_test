#!/usr/bin/env python3

node_name = "talker_exec"

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float64

class talker_exec(Node):

    def __init__(self, **kwargs):
        super().__init__(node_name, **kwargs)
        node_num = self.declare_parameter('node_num').value
        self.pub = self.create_publisher(Float64, "exec_pubsub_"+str(node_num), 1)
        self.create_timer(0.1, self.pub_f)

    def pub_f(self):
        msg = Float64()
        msg.data = float(time.time())
        self.pub.publish(msg)


def main(args=None):
    try:
        rclpy.init(args=args)
        node = talker_exec()
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
