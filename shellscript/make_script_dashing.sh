#!/bin/sh

cd ~/ros2/src/ros2_test/launch
find . -type f -exec sed -i "s/executable=/node_executable=/g" {} \;
find . -type f -exec sed -i "s/name=/node_name=/g" {} \;
find . -type f -exec sed -i "s/namespace=/node_namespace=/g" {} \;
