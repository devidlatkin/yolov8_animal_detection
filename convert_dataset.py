import os
import glob
import shutil
import imagesize
import argparse


ANIMALS_CLASS_ID = 0  # We have only 1 animals class id


def convert_to_yolo_format(x1, y1, x2, y2, image_width, image_height):
    center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
    width = x2 - x1
    height = y2 - y1
    center_x /= image_width
    center_y /= image_height
    width /= image_width
    height /= image_height
    return (center_x, center_y, width, height)


def get_yolo_annotation(img_path, label_path):
    width, height = imagesize.get(img_path)
    yolo_labels = []
    with open(label_path, 'r') as file:
        labels = file.read().split('\n')
        labels = [string for string in labels if string]  # remove empty strings
        for label in labels:
            label = label.split(' ')
            try:
                float(label[1])
            except:
                ''' If we have multiple classes inside one bbox or bbox is not well-defined, skip the sample '''
                return None
            x1, y1, x2, y2 = list(map(float, label[1:]))
            yolo_label = [str(ANIMALS_CLASS_ID), *list(map(str, convert_to_yolo_format(x1, y1, x2, y2, width, height)))]
            yolo_labels.append(' '.join(yolo_label))
    return yolo_labels


def convert_dataset_to_yolo_dataset(path_to_dataset, path_to_save):
    classes_names = os.listdir(path_to_dataset)
    class_to_id_map = dict()
    for i in range(len(classes_names)):
        class_to_id_map[classes_names[i]] = i

    path_to_save_images = os.path.join(path_to_save, 'images')
    path_to_save_labels = os.path.join(path_to_save, 'labels')

    if not os.path.isdir(path_to_save_images):
        os.makedirs(path_to_save_images)
    if not os.path.isdir(path_to_save_labels):
        os.makedirs(path_to_save_labels)

    for class_name in classes_names:
        curr_img_paths = glob.glob(os.path.join(path_to_dataset, class_name, '*'))
        for img_path in curr_img_paths:
            if not os.path.isfile(img_path):
                continue
            label_path = os.path.join(os.path.dirname(img_path), 'Label', os.path.basename(img_path).split('.')[0]+'.txt')
            if not os.path.isfile(img_path) or not os.path.isfile(label_path):
                raise RuntimeError(f'Image {img_path} or Label {label_path} is not exists! Dataset error occurred!')
            yolo_labels = get_yolo_annotation(img_path, label_path)
            if yolo_labels is None:
                continue
            shutil.copy(img_path, os.path.join(path_to_save_images, os.path.basename(img_path)))

            with open(os.path.join(path_to_save_labels, os.path.basename(label_path)), 'w') as file:
                for string in yolo_labels:
                    file.write(string + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')

    # Add arguments
    parser.add_argument('--read_path', type=str, default='./datasets/animals_detection',
                        help='The path to animals detection dataset.')
    parser.add_argument('--save_path', type=str, default='./datasets/yolo_animals_detection',
                        help='The path to save converted dataset.')
    args = parser.parse_args()

    if not os.path.isdir(args.read_path):
        print(f'Dataset path {args.read_path} is not exists! Please download it here or use the custom path.')

    path_to_read_train_dataset = os.path.join(args.read_path, 'train')
    path_to_read_test_dataset = os.path.join(args.read_path, 'test')

    path_to_save_train_dataset = os.path.join(args.save_path, 'train')
    path_to_save_test_dataset = os.path.join(args.save_path, 'test')

    print('Converting train datasets...')
    convert_dataset_to_yolo_dataset(path_to_read_train_dataset, path_to_save_train_dataset)
    print('Converting test datasets...')
    convert_dataset_to_yolo_dataset(path_to_read_test_dataset, path_to_save_test_dataset)
    print('Dataset was successfully converted!')
