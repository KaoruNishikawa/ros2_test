#!/bin/sh

# specify which file to launch #
launch_file=exec_test.launch.py
node_executor=exec_node.py
################################
######## configuration #########
################################
topic_num=120
group_num=xx
################################


# launch
sleep 1s
# for shift in 0 2 4 6 8 10 12 14 16 18 20
for shift in 0, ..., $group_num
do
    cd ~/ros2/src/ros2_test/executor
    num_per_group=`expr $topic_num / $group_num`
    sed -i "s/for.*/for i in range\($num_per_group\)\:/" $node_executor
    cd ../launch
    sed -i "s/shift.*/shift = $shift/" $launch_file
    sed -i "s/total_pairs.*/total_pairs = $topic_num/" $launch_file
    sed -i "s/nodes_per_group.*/nodes_per_group = $num_per_group/" $launch_file
    sleep 1s
    timeout -s SIGINT 115s ros2 launch $launch_file
    sleep 30s
done

# clean
cd ~/Documents
dirname=result_$(date "+%Y%m%d_%H%M%S")
mkdir -p $dirname/data
mv cpu_used_* ./$dirname/data/
mv cpu_temp_* ./$dirname/data/
mv mem_used_* ./$dirname/data/
mv net_count_* ./$dirname/data/
mv delay_* ./$dirname/data/

# record settings
mkdir -p $dirname/config
cp ~/ros2/src/ros2_test/* ./$dirname/config/
ros2 doctor --report >> ./$dirname/ros2_configuration.txt

# back to where I was
cd ~/ros2/src/ros2_test/shellscript
