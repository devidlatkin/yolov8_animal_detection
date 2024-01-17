from ultralytics import YOLO

# Load a COCO pretrained model
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='animals.yaml', epochs=100, imgsz=640)