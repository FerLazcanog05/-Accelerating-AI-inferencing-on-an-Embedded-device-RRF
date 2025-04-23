# Summary of Research

# # Project Overview


The goal of our project is to make AI run faster on small devices, especially for real-time object detection. That means finding the right hardware and software to help us run AI models directly on the device, instead of relying on big cloud servers. We chose the NVIDIA Jetson Orin Nano Developer Kit because it's powerful enough to handle AI tasks, doesn't use too much energy, and is pretty affordable, making it a great fit for edge computing projects like this one.

# # Hardware Options

# # # 1. NVIDIA Jetson Orin Nano Developer Kit

•	Specifications:

o	GPU: 1024-core NVIDIA Ampere architecture with 32 Tensor Cores

o	CPU: 6-core Arm Cortex-A78AE v8.2 64-bit

o	Memory: 8GB 128-bit LPDDR5

o	AI Performance: Up to 67 TOPS

o	Power Consumption: Configurable between 7W and 15W

o	Interfaces: USB 3.2, PCIe Gen 3, MIPI CSI-2 camera connectors


•	Features:

o	Supports multiple camera inputs

o	High-speed interfaces suitable for various peripherals

o	Compact form factor ideal for embedded applications

•	Resources:

o	NVIDIA Jetson Orin Nano Developer Kit
o	Jetson Orin Nano Developer Kit User Guide
o	Hardware Specifications

# # Software Tools and Frameworks

# # # 1. Operating System and SDK

JetPack SDK: This is NVIDIA’s all-in-one software bundle made for Jetson devices. It gives us everything we need to get started with AI—like the Ubuntu operating system, tools to run code on the GPU (like CUDA), and libraries that help with deep learning (like TensorRT and cuDNN). It also includes support for using cameras and videos. Basically, it’s the main setup you need to build and run AI projects on the Jetson Orin Nano.

o	CUDA Toolkit

o	cuDNN

o	TensorRT

o	DeepStream SDK

o	Multimedia APIs

•	Features:

o	Flexibility to run any Linux Kernel

o	Wider options of Linux-based distributions

o	Ability to update Jetson AI Stack independently

# # •	Resources:

o	JetPack SDK

o	JetPack 6 Developer Guide

# # # 2. Deep Learning Frameworks

PyTorch: A well-known AI library that’s really easy to use, especially when you're learning or trying out new ideas. It’s popular because it lets you build and test models in a simple, step-by-step way, so you can see what’s going on while your AI is running. That makes it great for experimenting and learning how things work.

# # # PyTorch Official Website

TensorRT: This is a tool from NVIDIA that helps make AI models run faster and more efficiently, especially on devices like the Jetson Orin Nano. It does things like converting the model to use lower precision (like FP16 or INT8 instead of full 32-bit), and combining layers in the model (called layer fusion) to cut down the time it takes to run. It’s really helpful when you want your AI to make quick predictions in real-time without using too much memory.

o	Precision calibration (FP16/INT8)

o	Kernel auto-tuning

o	TensorRT Overview

o	TensorRT Documentation


# # # 3. Computer Vision Libraries

OpenCV: An open-source (free) library that helps us work with images and videos. In our project, we use it to grab video from the camera, edit or prepare the images (like resizing or turning them into grayscale), and draw boxes around things the AI detects. It’s super useful for managing all the visual stuff in our object detection system.

# # OpenCV Installation on Orin Nano

# # # 4. Object Detection Models
YOLOv5: A super fast and accurate model for detecting objects in real time. It can quickly spot and label things in images or live video, which makes it perfect for devices like the Jetson Orin Nano. Even though it runs on a smaller device, it still gives good results and is easy to work with, so it’s a solid choice for our project.

# # YOLOv5 GitHub Repository

# # YOLOv5 Documentation

# # Training YOLOv5 on Custom Dataset



Additional Resources and References

•  NVIDIA Developer Tools: A set of tools from NVIDIA that help you check how your program is performing. They’re useful for finding and fixing problems (debugging), making things run faster (optimization), and understanding how your code uses the GPU.

🔗 NVIDIA Developer Tools

•  Pretrained Models Repository: A GitHub page with a bunch of ready-to-use computer vision models and example code. It's a good starting point for testing object detection without having to train a model from scratch.

🔗 CV-pretrained-model GitHub Repository

•  NVIDIA Optimized Frameworks: Official documentation showing which popular AI frameworks (like PyTorch and TensorFlow) are specially optimized to work faster on NVIDIA devices like Jetson.

🔗 NVIDIA Optimized Frameworks
