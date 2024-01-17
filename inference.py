from ultralytics import YOLO
import argparse


def inference(path_to_checkpoint, path_to_image_src):
    model = YOLO(path_to_checkpoint)
    model.predict(path_to_image_src, save=True, imgsz=640, conf=0.6)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')

    # Add arguments
    parser.add_argument('--checkpoint_path', type=str, default='./runs/detect/2024_01_17_animals_detection/weights/best.pt',
                        help='The path to read a checkpoint')
    parser.add_argument('--image_src', type=str, default='./datasets/inference_dataset',
                        help='The path to directory of image/video to the inference')
    args = parser.parse_args()

    inference(args.checkpoint_path, args.image_src)