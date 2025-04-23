from ultralytics import YOLO
import cv2

# Load the TensorRT-optimized model
model = YOLO("yolov8n.pt")
model.export(format="onnx")
# Live camera inference
for result in model(source=0, stream=True):
    frame = result.plot()
    cv2.imshow("YOLOv8 TRT", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
