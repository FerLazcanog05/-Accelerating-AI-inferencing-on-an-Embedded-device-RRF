#Detail Outline of Generic Workflow on Jetson Orin Nano


##Step 1: Hardware Setup
•	Device: NVIDIA Jetson Orin Nano
•	Camera: USB UVC-compatible webcam (e.g., Logitech C920)
•	Monitor: HDMI output or SSH connection
•	Peripherals: Keyboard, mouse, external storage (optional)
##Step 2: Initial System Configuration
•	OS: JetPack 6.x (Ubuntu 22.04.5 LTS with CUDA pre-installed)
•	Terminal Access: Via SSH or physical monitor and keyboard
##Step 3: Python Environment Setup
curl https://pyenv.run | bash
Add the following to ~/.bashrc:
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
Reload shell:
source ~/.bashrc
Install Python 3.9.0:
pyenv install 3.9.0
pyenv global 3.9.0
##Step 4: Verify CUDA & Install PyTorch
Verify CUDA Toolkit:
nvcc --version
Confirm PyTorch sees GPU:
python3 -c "import torch; print(torch.cuda.is_available())"
Install JetPack-compatible PyTorch (via NVIDIA):
pip install torch==2.5.0+nv24.04 torchvision==0.20.0+nv24.04 -f https://developer.download.nvidia.com/compute/redist/jp/v62/pytorch/torch.html
##Step 5: Clone & Set Up YOLOv5 (for testing)
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
##Step 6: Run Tests
Static image detection:
python detect.py --source data/images/bus.jpg --weights yolov5s.pt --conf 0.25
Live camera detection:
python detect.py --source 0 --weights yolov5s.pt --conf 0.25
##Step 7: Troubleshooting
•	Use v4l2-ctl to adjust camera settings (e.g., pixel format).
•	Add YUV to RGB conversion if needed.
•	If torch.cuda.is_available() is False:
o	Check CUDA and PyTorch compatibility.
o	Use dmesg to check GPU driver status.
o	Ensure you're using the correct wheel from NVIDIA.
If PyTorch remains incompatible with CUDA, consider switching to Ultralytics + TensorRT or ONNX workflows instead.




#After running into compatibility issues between PyTorch and CUDA on Jetson Orin Nano, we switched to using Ultralytics, a Python package that simplifies the entire
YOLOv8 workflow. Ultralytics integrates model loading, training, exporting, and inference while also supporting TensorRT and ONNX. This allowed us to streamline
installation, avoid version conflicts, and run real-time object detection using the onboard GPU. 
Codes from: https://docs.ultralytics.com/es/guides/nvidia-jetson/#install-pytorch-and-torchvision 

##Step1:Environment Setup-To Avoid conflict with previous configuration
python3 -m venv yolovenv
source yolovenv/bin/activate
We used a virtual environment to isolate packages and ensure reproducibility.
##Step2:Dependency Installation
pip install ultralytics
pip install onnx onnxruntime-gpu==1.20.0 onnx-simplifier
pip install numpy==1.23.5
pip install opencv-python
We used JetPack 6.2 compatible versions and downgraded NumPy to fix compatibility issues with onnxruntime.
##Step3:Jetson Performance Mode-since run into Cublas memory Allocation Problem
sudo nvpmodel -m 0
sudo jetson_clocks
Enables MAXN power mode and maximizes CPU/GPU clock speeds for optimal performance use yolo8n (lighther)
no improment, use onnxruntime-gpu
##Step4:Model Export Using Ultralytics
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.export(format="onnx")
We used the lightest YOLOv8n model for fast inference. The model was exported to ONNX for compatibility with TensorRT.
##Step5:Convert ONNX to TensorRT
trtexec --onnx=yolov8n.onnx --saveEngine=yolov8n.engine --fp16
This command uses NVIDIA's TensorRT engine to convert the ONNX model to an optimized GPU inference engine.
##Step6:Live Camera Inference Code
from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.engine")
for result in model(source=0, stream=True):
    frame = result.plot()
    cv2.imshow("YOLOv8 TensorRT", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
This script streams input from the USB camera, runs detection, and displays annotated output.
Step7:GPU Verification Tools
sudo pip3 install -U jetson-stats
jtop
We used jtop to monitor GPU load and M2M activity. We also used tegrastats to monitor deeper-level GPU memory usage.
Even if jtop shows 0k GPU MEM for Python PID, TensorRT uses shared CUDA contexts, and GPU activity is confirmed via:
•	GPU% spike
•	M2M memory usage
