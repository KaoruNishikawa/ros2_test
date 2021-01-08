#!/bin/sh

# specify which file to launch #
launch_file=exec_test.launch.py
node_executor=exec_node.py
################################
######## configuration #########
################################
export ROS_DOMAIN_ID=17
shift=1
topic_num=120
################################


# launch
sleep 1s
# for group_num in 1 2 3 4 5 6 10 12 15 20 30 60  # 60 = 2^2 3 5 ; 3*2*2=12
for group_num in 1 2 3 4 5 6 8 10 12 15 20 24 30 40 60 120  # 2^3 3 5 ; 4*2*2=16
do
    cd ~/ros2/src/ros2_test/ros2_test
    num_per_group=`expr $topic_num / $group_num`
    sed -i "s/for i in.*/for i in range\($num_per_group\)\:/" $node_executor
    cd ../launch
    sed -i "s/shift =.*/shift = $shift/" $launch_file
    sed -i "s/total_pairs =.*/total_pairs = $topic_num/" $launch_file
    sed -i "s/nodes_per_group =.*/nodes_per_group = $num_per_group/" $launch_file
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
cp -r ~/ros2/src/ros2_test/* ./$dirname/config/
ros2 doctor --report >> ./$dirname/ros2_configuration.txt

# record ntp state
mkdir -p $dirname/stats
cp -r /var/log/ntpstats/* ./$dirname/stats/

# back to where I was
cd ~/ros2/src/ros2_test/shellscript
