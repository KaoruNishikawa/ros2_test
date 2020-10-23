#!/bin/sh

# specify which file to launch
launch_file=launch_node_only_test.py

# build
cd ~/ros2
colcon build --symlink-install
. ./install/setup.bash

# launch
cd src/ros2_test/launch

# node_num = 1
sed 's/\sfor.*/for i in range\(1\)\:' $launch_file
(sleep 100; kill $$)&
ros2 launch $launch_file

# node_num = 20
sed 's/\sfor.*/for i in range\(20\)\:' $launch_file
(sleep 100; kill $$)&
ros2 launch $launch_file