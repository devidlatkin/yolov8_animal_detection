from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')


# results = model(['/home/devid/Documents/all_docs/personal/bayanat/task_share/test/animals/animal_1.jpg', '/home/devid/Documents/all_docs/personal/bayanat/task_share/test/animals/animal_2.jpg'])  # return a list of Results objects
# results = model('/home/devid/Documents/all_docs/personal/bayanat/task_share/test/animals/')  # return a list of Results objects
#
# print(results)
# # Process results list
# for result in results:
#     boxes = result.boxes  # Boxes object for bbox outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs


model.predict('/home/devid/Documents/all_docs/personal/bayanat/task_share/test/animals/', save=True, imgsz=640, conf=0.5)