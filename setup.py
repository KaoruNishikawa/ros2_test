from setuptools import setup

package_name = 'ros2_test'

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
            'mem_cpu_checker='+package_name+'.node_num_test_cpu_mem:main',
        ],
    },
)
