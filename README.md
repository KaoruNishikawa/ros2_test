# ros2_test

## About this package

This package provides:

- ROS 2 nodes for testing ROS 2 performance;
  - CPU usage
  - CPU temperature
  - Memory usage
  - Latency
  - Amount of network communications
- A notebook for analysing the data and draw figures.

## Installation

```shell
git clone https://github.com/kaorunishikawa/ros2_test.git path/to/somewhere/in/your/machine/
```

If you need the previous version:

```shell
git clone -b v1.0.0 https://github.com/kaorunishikawa/ros2_test.git path/to/somewhere/in/your/machine/
```

## Usage

### Run Performance Test

- Executor configuration in 1 PC:

```shell
. exec_bunch_num_test.sh <NUM>
```

where `<NUM>` is number of dummy pub/sub pairs to launch. With some ROS 2 nodes launched, this command can test the load of the nodes assigning the number 0:

```shell
ros2 launch <arbitrary launch file>
. exec_bunch_num_test.sh 0
```

The data is recorded in your `~/Documents/result_(date and time)` directory. The path is displayed at the top and the last line of the terminal.

<img width="466" alt="スクリーンショット 2021-03-31 19 04 44" src="https://user-images.githubusercontent.com/68896036/113128074-625b7080-9254-11eb-890f-b1ddfa6c06cc.png">

### Analyse the Data

This analysis tool uses xarray and other packages. Please configure the environment using

```shell
poetry install
```

or install them manually (list of packages needed is in `[tool.poetry.dependencies]` section of `pyproject.toml`).

Open `analysis/analysis.ipynb`, specify where the data is stored, and run `draw_figure(path)`.

## Enhancement

To test multiple machines performance, 

- comment out or configure Publisher nodes or Subscriber nodes accordingly (avoid conflict of node name, etc.) in `ros2_test/exec_node.py`
- assign an environment variable `ROS_DOMAIN_ID` if needed
- *remote launch* (using the shell script or launch file) the nodes via `shellscript/ros2_performance_test.sh`
