# ROS2 Safety Monitoring and Mitigation Framework

A modular, real-time distributed data pipeline built natively on **ROS2 Jazzy Jalisco (Ubuntu 24.04 LTS)**. This framework simulates continuous vehicle telemetry from an Unmanned Ground Vehicle (UGV) operating over rugged terrain, dynamically evaluating physical stability constraints to mitigate vehicular hazards and enhance field operational safety.

## System Architecture

The package is designed around an asynchronous **Publisher/Subscriber** topology leveraging standard ROS2 middleware and DDS communication layers.
