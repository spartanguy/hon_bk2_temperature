from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'spartan_ros2_package'

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
    description='Hőmérséklet riasztás: Temperature Generator Node: szimulált hőmérsékleti adatokat generál és publikál egy topicon. Alert Node: feliratkozik a hőmérsékleti adatokra, és riasztást küld egy másik topicon, ha a hőmérséklet meghalad egy megadott küszöbértéket.',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'control_vehicle = spartan_ros2_package.control_vehicle:main',
        ],
    },
)
