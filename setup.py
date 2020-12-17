from setuptools import setup

package_name = 'ros2_test'

scripts = [
    'dummy_sub',
    'dummy_node',
    'exec_recording_nodes_S',
    'exec_recording_nodes_M',
    'exec_dummy_nodes',
    'dummy_node_exec',
    'talker_exec',
    'listener_exec',
    'exec_pubsub_nodes',
    'exec_param_talker',
    'check_cpu',
    'check_mem',
    'check_net',
    'check_temp',
    'exec_checker',
    'node_publish',
    'node_subscribe',
    # 'exec_node',
]
executors = [
    'exec_node',
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
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amigos',
    maintainer_email='amigos@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher='+package_name+'.delay_test_pub:main',
            'subscriber='+package_name+'.delay_test_sub:main',
            'node_num_pub='+package_name+'.node_num_test_pub:main',
            'node_num_sub='+package_name+'.node_num_test_sub:main',
            'cpu_checker='+package_name+'.node_num_test_cpu:main',
            'mem_checker='+package_name+'.node_num_test_mem:main',
            'net_checker='+package_name+'.node_num_test_net:main',
            'node_num_sub_m='+package_name+'.node_num_test_sub_m:main',
            # 'dummy_sub='+package_name+'.dummy_sub:main',
            # 'dummy_node='+package_name+'.dummy_node:main',
            'topic_num_pub='+package_name+'.topic_num_test_pub:main',
            'topic_num_sub='+package_name+'.topic_num_test_sub:main',
            #'exec_recording_nodes_S='+package_name+'.exec_recording_nodes_S:main',
            #'exec_recording_nodes_M='+package_name+'.exec_recording_nodes_M:main',
            #'exec_dummy_nodes='+package_name+'.exec_dummy_nodes:main',
            #'dummy_node_exec='+package_name+'.dummy_node_exec:main',
            #'talker_exec='+package_name+'.talker_exec:main',
            #'listener_exec='+package_name+'.listener_exec:main',
            #'exec_pubsub_nodes='+package_name+'.exec_pubsub_nodes:main',
            'talker_executable='+package_name+'.talker_exec:main',
            #'exec_param_talker='+package_name+'.exec_param_talker:main',
            #'check_cpu='+package_name+'.check_cpu:main',
            #'check_mem='+package_name+'.check_mem:main',
            #'check_net='+package_name+'.check_net:main',
            #'check_temp='+package_name+'.check_temp:main',
            #'exec_checker='+package_name+'.exec_checker:main',
            #'node_publish='+package_name+'.node_publish:main',
            #'node_subscribe='+package_name+'.node_subscribe:main',
            #'exec_node='+package_name+'.exec_node:main',
        ] + [
            f'{name}={package_name}.{name}:main' for name in scripts
        ] + [
            f'{name}={package_name}.{name}:main' for name in executors
        ],
    },
)
