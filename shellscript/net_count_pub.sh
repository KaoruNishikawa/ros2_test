#!/bin/sh

# keep original
ROS_DOMAIN_ID_ORIGINAL=${ROS_DOMAIN_ID}

# specify which file to launch #
launch_pub=net_count_pub.launch.py
################################
######## configuration #########
################################
export ROS_DOMAIN_ID=20
################################


# launch
sleep 1s

for sub_num in 1 2 3 4 5 10 30 50 100
do
    cd ~/ros2/src/ros2_test/launch
    sed -i "s/for i in.*/for i in range\($sub_num\)\:/" $launch_pub
    sleep 1s
    timeout -s SIGINT 100s ros2 launch $launch_pub
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

export ROS_DOMAIN_ID=${ROS_DOMAIN_ID_ORIGINAL}
