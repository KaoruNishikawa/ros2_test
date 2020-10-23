#!/bin/sh

# specify which file to launch
launch_file=launch_node_only_test.py

# build
cd ~/ros2
colcon build --symlink-install
. ./install/setup.bash

# launch
cd src/ros2_test/launch
sleep 5s

# 
node_num=1
echo start testing with $node_num node\(s\)
sed -i "s/\sfor.*/for i in range\($node_num\)\:/" $launch_file
sleep 1s
timeout 100s ros2 launch $launch_file
sleep 15s

# 
node_num=20
echo start testing with $node_num node\(s\)
sed -i "s/\sfor.*/for i in range\($node_num\)\:/" $launch_file
sleep 1s
timeout 100s ros2 launch $launch_file
sleep 15s

# back to initial directory
cd ./../shellscript