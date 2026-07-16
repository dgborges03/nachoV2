# NachoV2

NachoV2 is a personal mecanum-drive robot project that is built using Maxx 
"mpeccable" Ibarra's Ignacio platform (https://github.com/mpeccable/ignacio). Raspberry Pi 4 + RPLIDAR A1M8 + ROS2 
(Humble + Docker) working toward SLAM and autonomous navigation.

## Hardware

- Raspberry Pi 4 Model B
- 2x L298N dual motor drivers driving 4 mecanum wheels
- RPLIDAR A1M8 360° laser scanner
- 2x INR18650 battery pack (motor power) + dedicated 5V supply (Pi/LiDAR)

## Software

- ROS2 Humble, running in Docker
- Custom gpiozero-based motor control (mecanum kinematics, keyboard teleop via WASD + arrow keys)
- rplidar_ros for LiDAR integration
- Live visualization via Foxglove Studio over Tailscale
- Roadmap: slam_toolbox for mapping, nav2 for autonomous navigation

## Status

In development and it will be seen at OpenSauce B-)
