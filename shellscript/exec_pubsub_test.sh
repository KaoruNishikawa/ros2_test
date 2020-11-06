#!/bin/sh

# specify which file to launch
launch_file=launch_exec_PUBSUB.py

# build
cd ~/ros2
# colcon build --symlink-install
# . ./install/setup.bash
# sleep 5s

# launch
cd src/ros2_test/launch
sleep 1s
# 
for node_num in `seq 0 20`
do
    sed -i "s/for.*/for i in range\($node_num\)\:/" $launch_file
    sleep 1s
    timeout -s SIGINT 100s ros2 launch $launch_file
    sleep 30s
    cd ~/Documents
    node_num=`printf "%03g" $((20*$node_num))`
    mv -i cpu_used.txt cpu_used_$node_num.txt && :
    mv -i mem_used.txt mem_used_$node_num.txt && :
    mv -i net_count.txt net_count_$node_num.txt && :
    mv -i test_node_num_*.txt delay_${node_num}_node.txt && :
    cd ~/ros2/src/ros2_test/launch
    sleep 5s
done

# clean
cd ~/Documents
dirname=result_$(date "+%Y%m%d_%H%M%S")_EXEC_PUBSUB
mkdir -p $dirname/data
mv cpu_used_* ./$dirname/data/
mv mem_used_* ./$dirname/data/
mv net_count_* ./$dirname/data/
mv delay_* ./$dirname/data/

# record settings
cp ~/ros2/src/ros2_test/shellscript/node_test.sh ./$dirname/
cp ~/ros2/src/ros2_test/launch/$launch_file ./$dirname/
mkdir ./$dirname/scripts
cp -r ~/ros2/src/ros2_test/ros2_test/* ./$dirname/scripts/
cp ~/ros2/src/ros2_test/setup.py ./$dirname/
cp ~/ros2/src/ros2_test/package.xml ./$dirname/
ros2 doctor --report >> ~/Documents/$dirname/ros2_configurations.txt

# back to initial directory
cd ~/ros2/src/ros2_test/shellscript