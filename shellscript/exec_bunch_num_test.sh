#!/bin/sh

# specify which file to launch #
launch_file=exec_test.launch.py
node_executor=exec_node.py
################################
######## configuration #########
################################
# export ROS_DOMAIN_ID=17
export ROS2_TEST_SHIFT=0
export ROS2_TEST_TOPIC_NUM=$1
################################

if !(type ros2 > /dev/null 2>&1)
then
    echo "ros2 command not defined"
    exit 1
fi

my_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# get divisors of $ROS2_TEST_TOPIC_NUM
divisors=()
if [ $ROS2_TEST_TOPIC_NUM == 0 ]
then
    divisors+=(1)
else
    for i in `seq 1 $ROS2_TEST_TOPIC_NUM`
    do
        if [ $(($ROS2_TEST_TOPIC_NUM % $i)) == 0 ]
        then
            divisors+=($i)
        fi
    done
fi

# data directory
export ROS2_TEST_SAVE_DIR=$HOME/Documents/result_$(date "+%Y%m%d_%H%M%S")
mkdir -p $ROS2_TEST_SAVE_DIR

# launch
for group_num in ${divisors[@]}
do
    export ROS2_TEST_NUM_PER_GROUP=`expr $ROS2_TEST_TOPIC_NUM / $group_num`
    cd $my_dir/../launch
    sleep 1s
    timeout -s SIGINT 15s ros2 launch $launch_file
    sleep 5s
done

# record settings
mkdir -p $ROS2_TEST_SAVE_DIR/config
cp -r $my_dir/../* $ROS2_TEST_SAVE_DIR/config/
ros2 doctor --report >> $ROS2_TEST_SAVE_DIR/ros2_configuration.txt || :

# record ntp state
mkdir -p $ROS2_TEST_SAVE_DIR/stats
cp -r /var/log/ntpstats/* ./$ROS2_TEST_SAVE_DIR/stats/ || :

# back to where I am
cd $my_dir

unset ROS2_TEST_SHIFT
unset ROS2_TEST_TOPIC_NUM
unset ROS2_TEST_SAVE_DIR
unset ROS2_TEST_NUM_PER_GROUP
