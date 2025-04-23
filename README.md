# 1. Problem Statement and Discussion

Real-time object detection is a critical component in many intelligent systems, including autonomous vehicles, industrial automation, security surveillance, and smart cities. The ability to not only recognize but also localize multiple objects within a scene enables machines to make fast, context-aware decisions.


Traditionally, such AI-based processing is handled in the cloud due to the high computational demands. However, cloud-based inference introduces latency due to the need for constant communication between local devices and remote servers. In time-sensitive applications, like robotics or self-driving cars, such delays can pose serious challenges.


Edge computing presents a promising alternative. By shifting AI workloads to local hardware, we eliminate dependence on network speed and cloud infrastructure. In this project, we leverage the NVIDIA Jetson Orin Nano, a compact yet powerful embedded system equipped with a GPU optimized for AI tasks. Our goal is to demonstrate real-time object detection using a live camera feed and highlight the performance benefits achieved through parallel processing and GPU acceleration at the edge.


# 2. Initial Configuration and Setup

The following steps summarize the setup of the Jetson Orin Nano for this project:

Operating System:

Installed Ubuntu 22.04.5 through NVIDIA JetPack 6.x, which comes with necessary drivers, libraries, and development tools.


Python Environment:

Set up using pyenv to ensure compatibility with JetPack and TensorRT versions. Python 3.9 was selected to match dependencies.


Camera Configuration:

Used OpenCV to interface with the CSI or USB camera and capture real-time video frames.

Software Installations:

CUDA Toolkit

cuDNN (CUDA Deep Neural Network library)

PyTorch (Jetson-compatible build)

TorchVision

OpenCV (with GStreamer support for camera handling)

YOLOv5 repository (with ONNX export support)

TensorRT (for model optimization)

Nsight Systems and Compute for performance profiling


# 3. Hardware and Software Components
Hardware:
Jetson Orin Nano Developer Kit

USB or CSI Camera

MicroSD or NVMe storage for OS and dependencies

Active cooling (fan or heatsink)

Power supply (rated ≥ 5V/4A)


Software Frameworks and Libraries:

CUDA Toolkit – Enables general-purpose GPU computing.

cuDNN – Accelerates deep learning primitives like convolutions.

TensorRT – Optimizes and accelerates AI inference.

PyTorch & TorchVision – Deep learning framework and vision models.

OpenCV – Handles video capture, preprocessing, and visualization.

YOLOv5 – Object detection framework.

ONNX Runtime – Optional for model deployment in a lightweight, cross-framework way.

Nsight Systems/Compute – For performance debugging and bottleneck identification.



# 4. Choice of Pre-Trained Models and Rationale

For this project, we selected YOLOv5s (small variant) as the object detection model. The reasoning behind this choice includes:

Speed: YOLOv5s is optimized for real-time performance and runs smoothly on embedded GPUs with limited resources.

Accuracy: Offers a solid balance between speed and accuracy, suitable for many practical scenarios.

Lightweight: Requires less memory and compute, making it ideal for the Jetson Orin Nano's embedded environment.

ONNX Export Support: Easily exportable to the ONNX format for use with TensorRT.

Community Support: Well-documented with a large open-source community, simplifying troubleshooting and customization.

In future iterations, we may explore other variants like YOLOv8 or EfficientDet for use cases demanding either higher speed or improved accuracy.
