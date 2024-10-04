cmake_minimum_required(VERSION 3.5)
project(hon_bk2_temperature)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(PROGRAMS
  hon_bk2_temperature/temperature_generator.py
  hon_bk2_temperature/alert_node.py
  DESTINATION lib/${PROJECT_NAME})

ament_package()