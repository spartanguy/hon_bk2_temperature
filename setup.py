from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'hon_bk2_temperature'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Honfi Botond',
    maintainer_email='hobot2002@gmail.com',
    description='Temperature Generator and Alert Nodes',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_generator = hon_bk2_temperature.temperature_generator:main',
            'alert_node = hon_bk2_temperature.alert_node:main',
        ],
    },
)
