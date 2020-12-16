#!/bin/sh


# specify which file to launch
launch_file=exec_test.launch.py
node_executor=exec_node.py
node_num=120
deviation=0


# launch
sleep 1s
for group in 1 2 3 4 5 6 8 10 12 15 20 24 30 40 60 120
do
    cd ~/ros2/src/ros2_test/ros2_test
    index=`expr 120 / $group`
    sed -i "s/for.*/for i in range\($index\)\:/" $node_executor
    sed -i "s/dev =.*/dev = $deviation/" $node_executor
    cd ../launch
    sed -i "s/for.*/for i in range\($group\)\:/" $launch_file
    sleep 1s
    timeout -s SIGINT 115s ros2 launch $launch_file
    sleep 30s
    cd ~/Documents
    mv cpu_used.txt cpu_used_g${group}xi${index}.txt && :
    mv cpu_temp.txt cpu_temp_g${group}xi${index}.txt && :
    mv mem_used.txt mem_used_g${group}xi${index}.txt && :
    mv net_count.txt net_count_g${group}xi${index}.txt && :
    mv delay.txt delay_g${group}xi${index}.txt && :
    sleep 1s
done

# clean
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

