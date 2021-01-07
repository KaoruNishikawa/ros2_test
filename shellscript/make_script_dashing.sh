#!/bin/sh

cd ~/ros2/src/ros2_test/launch
find . -type f -exec sed -i "s/executable/node_executable/g" {} \;
