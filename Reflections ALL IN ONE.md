# Ruber Reflection

This project made me realize how powerful and complicated it is to implement an AI model in embedded systems. The version compatibility problem, especially between PyTorch and CUDA, and Jetson hardware,
was a major hurdle. Installation of a GPU-supported version of PyTorch was tedious and caused memory errors very often. Besides that, we had to deal with NumPy incompatibilities especially with ONNX and PyTorch
extensions, which required careful version control.

We couldn't always rely upon GPU monitoring tools. For instance, jtop showed completely wrong values despite being use of TensorRT when noting down memory usage. So we had to find other tools such as tegrastats
for accurate monitoring of the system. On the camera side, real-time video integration posed challenges, with color mismatches and some frame drops that we resolved using tools like v4l2-ctl and some tuning in
OpenCV.
There was a lot of trial and error when attempting to export the models into ONNX and TensorRT from YOLOv8. The process was laden with simplifications through the help of Ultralytics; however, many CUDA memory 
allocation issues made the process quite a hassle as we had to experiment on how to export and simplify the models in a step-by-step fashion.

The technical setbacks notwithstanding, the Jetson Orin Nano showed what on-edge AI is for, allowing us to run real-time object detection locally without dependence on any cloud service. This meant lower latency, 
better privacy, and more dependability. 

It may not only really improve inference speed while consuming fewer resources, but also fit robotics, smart cameras, and low-power deployments. When paired with innovative tools like Ultralytics and ONNX,
the Jetson platform showed itself to be a small but mighty power house for rapid prototyping with AI.

Final Thoughts

This taught us to persevere, to manage our versions, and to understand the system behavior of embedded AI. More than that, it proved how affordable and pragmatic edge computing has become, especially with key
players in the industry that drive the vision such as Jetson.


# Fernando Lazcano Reflection

## 1. New Concepts, Skills, and Tools Learned:

During this project, I got to work with a lot of new tools I hadn’t used before, like NVIDIA JetPack, TensorRT, and ONNX—which are used to make AI models run faster and more efficiently. I also improved my skills with PyTorch and OpenCV, especially for handling live camera feeds and doing real-time object detection. One of the coolest parts was learning how to actually set up and use the Jetson Orin Nano, a small device with a built-in GPU. Getting it to run the AI model properly taught me a lot about how edge computing works.

I also got better at understanding how GPU acceleration works and ran into a bunch of issues with installing the right versions of software like CUDA and PyTorch. Figuring out how to fix those problems helped me get more confident in debugging and troubleshooting. These are all things I can use in other school projects—especially anything with embedded systems or AI—and they’ll definitely be useful in the kind of tech jobs I want in the future.

## 2. Project Successes and What Worked Well:

One thing that went really well was getting the object detection to run in real time on the Jetson Orin Nano using YOLOv5. A big reason this worked out was because I didn’t try to do everything all at once—I first made sure everything ran smoothly on my computer before moving it to the Jetson. Keeping track of what I installed and what worked (or didn’t) also saved me a ton of time. I used online forums, GitHub pages, and community posts whenever I hit a wall, which made a big difference when troubleshooting.

## 3. Challenges and What I Did to Solve Them:

The hardest part was setting up the Jetson environment. There were so many small version issues—like CUDA not matching the right version of PyTorch—and it took a lot of Googling, trial and error, and reading forum threads to get everything working. Another challenge was making sure the live camera feed didn’t slow everything down, especially since the Jetson has limited resources compared to a regular computer.

I took the lead on setting up the Jetson, making sure all the dependencies and software were installed properly. I also built and tested the object detection system and helped fix problems along the way. I spent a lot of time looking up solutions, testing different fixes, and figuring out how to apply them to our setup. I feel like I really owned that part of the project.
