#!/bin/sh

# specify which file to launch
launch_file=launch_node_only_test.py

# build
cd ~/ros2
# colcon build --symlink-install
# . ./install/setup.bash
# sleep 5s

# launch
cd src/ros2_test/launch
sleep 1s

# 
for i in 1 20 40 60 80 100 120 140 160 180 200 220 240 260 280 300 320 340 360 380 400
do
    node_num=$i
    echo start testing with $node_num node\(s\)
    sed -i "s/for.*/for i in range\($node_num\)\:/" $launch_file
    sleep 1s
    timeout 100s ros2 launch $launch_file
    sleep 15s
done

# back to initial directory
cd ./../shellscript