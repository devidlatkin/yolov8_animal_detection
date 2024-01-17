Preinstallations
```bash
pip install ultralytics argparse imagesize gdown
```

Run fast demo
```bash
bash fast_demo.sh
```

Train from scratch

Please download kaggle animals detection algorithm from here:

https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset

Convert this dataset in a format that is suitable for coco

```bash
python convert_dataset.py
```

Adjust animals.yaml paths if needed

Run inference:
```bash
python inference.py
```

Inference from custom path or/and custom image source:
```bash
python inference.py --checkpoint_path <your/yolo/checkpoint> --image_src <your/image/source>
```

For any questions please contact Devid Latkin