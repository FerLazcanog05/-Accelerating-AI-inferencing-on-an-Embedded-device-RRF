# Ruber Reflection

This project made us realize how powerful and complicated it is to implement an AI model in embedded systems. The version compatibility problem, especially between PyTorch and CUDA, and Jetson hardware,
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
