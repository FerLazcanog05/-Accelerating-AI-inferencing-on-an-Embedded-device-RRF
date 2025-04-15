Problem Statement

Object detection is one of the main tasks in computer vision, and it's used in lots of real-time systems like self-driving cars, robots, security cameras, and smart factories. Basically, it means being able to recognize and label objects in images or live video. But doing this in real time takes a lot of processing power.
Usually, these kinds of AI tasks are run on powerful cloud servers. That works well, but it also comes with some issues, like needing a fast internet connection and dealing with delays when sending data back and forth. These delays can be a big problem for systems that need to make quick decisions on the spot.
That’s where edge computing comes in. Instead of sending data to the cloud, we can run AI models directly on small, powerful devices right where the data is being collected. In this project, we're working with the NVIDIA Jetson Orin Nano, which is a compact computer with a built-in GPU that’s great for running AI models faster.
The goal of our project is to build a working prototype that uses this device to detect objects in real time from a live camera feed. We're using pre-trained AI models, some optimized software tools, and measuring how much faster and more efficient everything becomes when we run it on the Jetson. By the end, we want to show how much of a performance boost we get using parallel processing and GPU acceleration on an embedded device.

Discussion

Running AI models for object detection works really well with parallel processing. That’s because each video frame can be handled on its own, and even within a single frame, we can split the work, like cleaning up the image, running the AI model, and drawing boxes around detected objects, so it all happens at the same time across different parts of the hardware.
The NVIDIA Jetson family, like the Jetson Orin Nano, is built for this kind of job. These devices have special parts like CUDA cores, Tensor cores, and AI accelerators that help take some of the load off the CPU and let things run much faster.

For this project, we explored some tools in NVIDIA’s ecosystem to help us out:

•	CUDA Toolkit: Helps us run tasks in parallel more efficiently.

•	TensorRT: Speeds up AI model inference by making it lighter and faster to run.

•	OpenCV: Takes care of handling the camera, images, and drawing results.

•	YOLOv5: A popular object detection model that works well even on small devices like ours.

•	Nsight Systems and Nsight Compute: Tools that let us measure performance and see where things might be slowing down.


By using the Jetson Orin Nano, we want to prove that we can run object detection in real-time on a small, portable device without needing the cloud. If it works well, this kind of setup could be used in lots of real-world projects where speed and mobility are important.
