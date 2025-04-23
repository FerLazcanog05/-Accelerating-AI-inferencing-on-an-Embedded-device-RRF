# Ruber Learning Plan

### Phase 1: Linux & Command Line Fundamentals

Begin by creating a solid grounding in Linux and its terminal environment. Learn to navigate through the Ubuntu file system while performing the common commands like cd, ls, pwd, and mkdir in the terminal,
and working with files like nano, vim, and cat. You should also be acquainted with user permissions, running commands with sudo, and managing software through package managers like apt or snap.
Understanding the design of file permission and user ownership (chmod, chown) will also be important. Some helpful resources are Linux Journey and the OverThe-Wire Bandit game for terminal exercises. 

### Phase 2: Getting Started with NVIDIA Jetson Platform

Familiarize yourself with the Jetson family, particularly Jetson Nano and Jetson Orin Nano. Get the architecture, GPU capabilities, memory, and GPIO layout. Learn the JetPack SDK, which bundles together all CUDA,
cuDNN, and TensorRT optimized for Jetson devices. Practice flashing your board with NVIDIA SDK Manager and monitor system performances using tools like jtop or tegrastats.
Use GitHub repositories such as JetsonHacks and the Jetson Zoo resource to check for software compatibility.

### Phase 3: Camera Integration with Jetson

Learn the interfacing of USB or CSI cameras with Jetson devices. Capturing live video using OpenCV by utilising cv2.VideoCapture(0) and learning how color formats (for instance YUV) are translated to RGB
will be the starter. Use utilities like v4l2-ctl, cheese, and guvcview to debug the camera input and configure it. In the spirit of performance, NVIDIA-accelerated pipelines through GStreamer should be reviewed. 

### Phase 4: YOLO and the AI Inference

Real-time object detection with YOLO is the next step. Begin with understanding the YOLO (You Only Look Once) model family, having major interest in the distinctions between YOLOv5 and YOLOv8. YOLOv8,
available via the Ultralytics library. Learn how to export YOLOv8 models to ONNX format and, therefore, convert them to TensorRT engines 
for faster GPU-based inference. Finally, check out some scripts that use cv2.imshow and model(source=0, stream=True) to visualize detections.

### Phase 5: Jetson Optimization & Deployment

Now that the detection is running, the next task is to optimize and automate it. Activate MAXN power mode via nvpmodel and jetson_clocks to unleash the full hardware performance. Supervise system activities
using either jtop or tegrastats. Any time the system boots, automatically start the inference script via systemd. Detections may be optionally logged, along with real-time FPS counters. Compare the performance 
between USB and CSI camera and accordingly optimize your system.
