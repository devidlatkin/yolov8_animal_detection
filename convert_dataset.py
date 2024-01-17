import os
import glob
import shutil
import imagesize

# path_to_dataset = '/home/devid/Documents/all_docs/personal/bayanat/train'
path_to_dataset = '/home/devid/Documents/all_docs/personal/bayanat/test'


# path_to_save = '/home/devid/Documents/all_docs/personal/bayanat/yolo_datasets/train'
path_to_save = '/home/devid/Documents/all_docs/personal/bayanat/yolo_datasets/test'

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
            print('label', label)
            try:
                float(label[1])
            except:
                ''' If we have multiple classes inside one bbox or bbox is not defined, skip the sample '''
                return None
            x1, y1, x2, y2 = list(map(float, label[1:]))
            yolo_label = [str(ANIMALS_CLASS_ID), *list(map(str, convert_to_yolo_format(x1, y1, x2, y2, width, height)))]
            yolo_labels.append(' '.join(yolo_label))
    return yolo_labels


def convert_dataset_to_yolo_dataset():
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
        print(f'Converting {class_name}...')
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