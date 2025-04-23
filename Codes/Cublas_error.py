from ultralytics import YOLO
import cv2
import torch

# Force model to GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Running on:", device)

model = YOLO("yolov8n.pt").to(device)

# Live inference from camera
for result in model(source=0, stream=True):
    frame = result.plot()
    cv2.imshow("YOLOv8", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
