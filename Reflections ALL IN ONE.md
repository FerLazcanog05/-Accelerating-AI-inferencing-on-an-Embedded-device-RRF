# Ruber Reflection

This project was a great opportunity for me to apply and deepen my technical skills while also identifying key gaps in my knowledge in embeeded systems. Although I had previously worked with YOLO in software environments, deploying it on Jetson hardware was a different challenge. I realized early on that my experience lacked the practical understanding required for Linux-based embedded deployment, version control across AI frameworks, and GPU optimization.

My individual contributions centered around researching YOLOv8 implementation on Jetson orin nano, testing model conversion processes, and troubleshooting imcompatibility errors. I was responsible for exporting the YOLOv8 model to ONNX format and attempting to convert it to TensorRT for real-time inference. One of the major setbacks our team faced was accidentally installing an incompatible version of PyTorch, which led to CUDA errors and broken dependencies. We spent time researching JetPack-compatible PyTorch builds and managing environment isolation to resolve these issues.

Additionally, I handled GPU performance monitoring. When jtop failed to report accurate memory usage during TensorRT inference, I discovered and implemented tegrastats as a more reliable alternative. I also configured the camera input and addressed real-time video stream issues such as frame drops and color format mismatches using tools like v4l2-ctl and OpenCV’s color conversion functions.

To close the skills gap, I created a structured learning plan divided into five key phases:

* Mastering the Linux terminal and file system with Linux Journey and OverTheWire Bandit

* Learning Jetson device architecture and flashing workflows via JetsonHacks GitHub

* Integrating USB/CSI cameras using OpenCV and v4l2 utilities

* Deploying YOLOv8 with Ultralytics, ONNX, and TensorRT

* Automating deployment using systemd, and optimizing performance with nvpmodel and jetson_clocks

Despite the technical setbacks, I successfully deployed a YOLOv8 model on the Jetson Orin Nano for real-time object detection. The final implementation was fast, fully offline, and required no cloud support, demonstrating the ability of low-latency, private, edge AI applications. This experience taught me not only how to manage version compatibility and system resources, but also how to troubleshoot under hardware constraints and design for real-world scalability.

This project proved that embedded AI is not only accessible, but increasingly practical for industry applications such as robotics, smart vision systems, and IoT. My hands-on involvement at every stage, from model research to hardware deployment, this significantly advanced my skill set and gave me a clearer picture of what it means to build robust, real-time AI systems on the edge.

# Fernando Lazcano Reflection

## 1. New Concepts, Skills, and Tools Learned:

During this project, I got to work with a lot of new tools I hadn’t used before, like NVIDIA JetPack, TensorRT, and ONNX, which are used to make AI models run faster and more efficiently. I also improved my skills with PyTorch and OpenCV, especially for handling live camera feeds and doing real-time object detection. One of the coolest parts was learning how to actually set up and use the Jetson Orin Nano, a small device with a built-in GPU. Getting it to run the AI model properly taught me a lot about how edge computing works.

I also got better at understanding how GPU acceleration works and ran into a bunch of issues with installing the right versions of software like CUDA and PyTorch. Figuring out how to fix those problems helped me get more confident in debugging and troubleshooting. These are all things I can use in other school projects, especially anything with embedded systems or AI, and they’ll definitely be useful in the kind of tech jobs I want in the future.

## 2. Project Successes and What Worked Well:

One thing that went really well was getting the object detection to run in real time on the Jetson Orin Nano using YOLOv5. A big reason this worked out was because I didn’t try to do everything all at once, I first made sure everything ran smoothly on my computer before moving it to the Jetson. Keeping track of what I installed and what worked (or didn’t) also saved me a ton of time. I used online forums, GitHub pages, and community posts whenever I hit a wall, which made a big difference when troubleshooting.

## 3. Challenges and What I Did to Solve Them:

The hardest part was setting up the Jetson environment. There were so many small version issues, like CUDA not matching the right version of PyTorch, and it took a lot of Googling, trial and error, and reading forum threads to get everything working. Another challenge was making sure the live camera feed didn’t slow everything down, especially since the Jetson has limited resources compared to a regular computer.

I took the lead on setting up the Jetson, making sure all the dependencies and software were installed properly. I also built and tested the object detection system and helped fix problems along the way. I spent a lot of time looking up solutions, testing different fixes, and figuring out how to apply them to our setup. I feel like I really owned that part of the project.


# Roberto Sejas
## Reflection
During this project, I gained more understanding in deploying AI models, more specifically object detection models, on embedded systems like the Jetson Nano. Our initial goal was to implement YOLOv5 for  object detection, trying to use the GPU available. But we had compatibility issues with CUDA, PyTorch, and Python versions, which made it difficult to get YOLOv5 running correctly. We were able to run it but only to the point were the CPU runned the object detection model but not the GPU.

Then we used YOLOv8 as an alternative, hoping it would be easier to use. But, once again dependency conflicts and and versions made it clear that the setup process was more complicated. We spend more 
time troubleshooting the versions and installations than working on the object detection. This  taught me how important it is to plan for software compatibility early in any project.

Then we started using Analytics version that already has compatible libraries and 
dependencies. This  reduced the setup time and helped us focus on start testing the camera and on how to make the detection faster through GPU. This showed me how simplifying work helps when developing an environment
to keep the project going on.

This project gaved me hands-on exposure with edge computing AI using live video while using 
the GPU performance metrics. Also working with Linux-based systems was a good practice, getting use to other type of
systems. Overall we had a lot of troubleshoot which was a good practice.


