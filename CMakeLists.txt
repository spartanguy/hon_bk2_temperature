cmake_minimum_required(VERSION 3.8)  
project(hon_bk2_temperature)  

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)


install(
    DIRECTORY ros2_py_template
    DESTINATION lib/${PROJECT_NAME}
)
ament_package()