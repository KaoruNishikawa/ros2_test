from pathlib import Path

from setuptools import setup

package_name = 'ros2_test'

scripts = [path.stem for path in Path("./ros2_test/nodes/").iterdir()]
executors = [
    path.stem for path in Path("./ros2_test/").iterdir()
    if not path.stem.startswith("_") and path.suffix
    # remove directories and __init__.py
]

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'numpy >= 1.19', 'xarray-dataclasses >= 0.3'],
    zip_safe=True,
    maintainer='Kaoru Nishikawa',
    maintainer_email='k.nishikawa@a.phys.nagoya-u.ac.jp',
    description='Performance test of ROS 2.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'{name}={package_name}.nodes.{name}:main' for name in scripts
        ] + [
            f'{name}={package_name}.{name}:main' for name in executors
        ]
        # 'console_scripts': [
        #     # 'publisher='+package_name+'.delay_test_pub:main',
        #     # 'subscriber='+package_name+'.delay_test_sub:main',
        #     # 'node_num_pub='+package_name+'.node_num_test_pub:main',
        #     # 'node_num_sub='+package_name+'.node_num_test_sub:main',
        #     # 'cpu_checker='+package_name+'.node_num_test_cpu:main',
        #     # 'mem_checker='+package_name+'.node_num_test_mem:main',
        #     # 'net_checker='+package_name+'.node_num_test_net:main',
        #     # 'node_num_sub_m='+package_name+'.node_num_test_sub_m:main',
        #     # 'topic_num_pub='+package_name+'.topic_num_test_pub:main',
        #     # 'topic_num_sub='+package_name+'.topic_num_test_sub:main',
        #     # 'talker_executable='+package_name+'.talker_exec:main',
        # ]
    },
)
