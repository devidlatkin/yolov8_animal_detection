This detector uses only 1 class called "Animal" for any animal detected. <br />
It uses Yolov8 model and was trained on the kaggle animals-detection-images. <br />
```bash
https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset
```

Examples:
![thomas-evans-NVXY8_M1n40-unsplash.jpg](runs%2Fdetect%2Fpredict%2Fthomas-evans-NVXY8_M1n40-unsplash.jpg)
![boris-smokrovic-lyvCvA8sKGc-unsplash.jpg](runs%2Fdetect%2Fpredict%2Fboris-smokrovic-lyvCvA8sKGc-unsplash.jpg)

Preinstallations:
```bash
pip install ultralytics argparse imagesize gdown
```

You can run fast demo with yolov8n model trained on 40 epochs with just one script:
```bash
bash fast_demo.sh
```

Train from scratch

1. Please download kaggle animals detection dataset from here:

https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset
```
And put it to:
```bash
yolov8_animal_detection/datasets/animals_detection
```

2. Convert this dataset in a format that is suitable for coco
```bash
python convert_dataset.py
```

3. Adjust animals.yaml paths if needed

Run inference:
```bash
python inference.py
```

Inference from custom path or/and custom image source:
```bash
python inference.py --checkpoint_path <your/yolo/checkpoint> --image_src <your/image/source>
```

For any questions please contact Devid Latkin: <br />
LinkedIn: https://www.linkedin.com/in/devid-latkin/  <br />
Telegram: @devid_latkin
