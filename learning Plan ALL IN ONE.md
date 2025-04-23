# Ruber Learning Plan

Throughout this project, I realized key gaps in my skills, particularly in working within a Linux environment and deploying AI models like YOLO on embedded hardware. Although I had previously used YOLO in software only environments, implementing it on a Jetson Nano exposed challenges I hadn’t faced before, such as camera integration, GPU optimization in hardware, and system-level deployment. These realizations led me to develop a structured learning plan to bridge these gaps and gain practical experience with real-time AI inference on edge devices.


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
available via the Ultralytics library. Learn how to export YOLOv8n models to ONNX format and, therefore, convert them to TensorRT engines 
for faster GPU-based inference. Finally, check out some scripts that use cv2.imshow and model(source=0, stream=True) to visualize detections.

### Phase 5: Jetson Optimization & Deployment

Now that the detection is running, the next task is to optimize and automate it. Activate MAXN power mode via nvpmodel and jetson_clocks to unleash the full hardware performance. Supervise system activities
using either jtop or tegrastats. Any time the system boots, automatically start the inference script via systemd. Detections may be optionally logged, along with real-time FPS counters. Compare the performance 
between USB and CSI camera and accordingly optimize your system.

# Fernando Lazcano Learning Plan

## 1. Identified Knowledge Gaps and Experience Needs:
Several knowledge gaps appeared during the development and testing of the real-time object detection system with the NVIDIA Jetson Orin Nano. For instance, CUDA programming and GPU memory management were rendered much more difficult to master for optimization of the inference performance of the models. Successful implementation was done in PyTorch and YOLOv5; however, ONNX conversion and TensorRT acceleration implementations highlighted a lack of experience in optimization techniques and hardware-specific deployment. Also, integration problems, as camera feed troubleshooting using OpenCV on embedded Linux, emerged from several challenges having to do with device drivers and frame processing.

## 2. Skills and Expertise Needed for Industry Implementation or Scaling:
Furthermore, in order to scale the above solution into an extended project or industrial application, additional skill sets would be of major importance. These would include:
Advanced model optimization, such as TensorRT and quantization methods (FP16/INT8).
Embedded systems development, including real-time operating systems and cross-compilation workflows.
DevOps and CI/CD practices for efficient code handling, deployment automation, and system reliability assurance.
Data pipeline designing for the effective handling and preprocessing of larger crowds of image or video data.
Cybersecurity best practices to safeguard edge devices against vulnerabilities in the field.

## 3. Training and Resources to Get Equipped:
Gaps will be closed and capabilities supersized by seeking any or all of the following interventions and training: NVIDIA Deep Learning Institute (DLI) courses on Jetson AI Fundamentals, CUDA programming, and TensorRT deployment. 

Coursera and Udemy courses on Embedded Linux, OpenCV, and advanced topics for PyTorch.

JetsonHacks, Qengineering, and official NVIDIA forums offer tutorials, troubleshooting guides, and active developer communities. 

Hands-on mini-projects that focus on deploying different AI models across varied embedded devices.

Collaboration among peers and mentors, especially with those who have experience in deploying edge AI systems in production environments. 

This plan will see to it that the gaps in knowledge are filled in but also that long-term skills for scaling edge AI systems in real environments will be built.

# Roberto Learning Plan

I can definitely get better at confirming the packages compatibility and optimizing AI models. 
I will like to be more capable with new model conversion techniques like ONNX and TensorRT,
which are new to me but still important for neural networks on embedded devices.

A good way if improving is by watching tutorials and practicing on my own through those tutorials
to gain more experience. There are also NVIDIA’s online courses for the Jetson, on how to do inferencing correctly
through TensorRT. I’ll look for more projects on edge comuting AI, so I can see how it properly
comes to life in the real world.

Finally, I want to practice running simple projects on other platforms and learn how to use better
tools like jtop, and Nsight Systems. These are useful to analyze performance 
and optimize the system even more.

