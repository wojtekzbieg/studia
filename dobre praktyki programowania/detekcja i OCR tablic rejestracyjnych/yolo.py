import os
import shutil
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split
from ultralytics import YOLO
import yaml

IMAGES_SOURCE_DIR = 'photos'
XML_FILE = 'annotations.xml'
DATASET_DIR = 'yolo_dataset'

def convert_to_yolo_bbox(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

def prepare_dataset():
    if os.path.exists(DATASET_DIR):
        shutil.rmtree(DATASET_DIR)

    for split in ['train', 'val']:
        os.makedirs(os.path.join(DATASET_DIR, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(DATASET_DIR, split, 'labels'), exist_ok=True)

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    data = []

    for image in root.findall('image'):
        name = image.get('name')
        width = int(image.get('width'))
        height = int(image.get('height'))

        for box in image.findall('box'):
            is_plate = False
            for attr in box.findall('attribute'):
                if attr.get('name') == 'plate number':
                    is_plate = True
                    break

            if is_plate:
                xtl = float(box.get('xtl'))
                ytl = float(box.get('ytl'))
                xbr = float(box.get('xbr'))
                ybr = float(box.get('ybr'))

                yolo_bbox = convert_to_yolo_bbox((width, height), (xtl, xbr, ytl, ybr))
                data.append((name, yolo_bbox))
                break

    train_data, val_data = train_test_split(data, test_size=0.3, random_state=42)

    def save_split(split_data, split_name):
        print(f"Przygotowywanie {split_name} ({len(split_data)} zdjęć)")
        for filename, bbox in split_data:
            src_img = os.path.join(IMAGES_SOURCE_DIR, filename)
            if not os.path.exists(src_img): continue

            dst_img = os.path.join(DATASET_DIR, split_name, 'images', filename)
            shutil.copy(src_img, dst_img)

            label_file = os.path.splitext(filename)[0] + '.txt'
            dst_label = os.path.join(DATASET_DIR, split_name, 'labels', label_file)

            with open(dst_label, 'w') as f:
                f.write(f"0 {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n")

    save_split(train_data, 'train')
    save_split(val_data, 'val')

    yaml_content = {
        'path': os.path.abspath(DATASET_DIR),
        'train': 'train/images',
        'val': 'val/images',
        'names': {0: 'license_plate'}
    }

    with open('data.yaml', 'w') as f:
        yaml.dump(yaml_content, f)

    print("Dataset gotowy")

def train_model():
    model = YOLO('yolo11n.pt')

    print("Poczatek treningu")

    model.train(
        data='data.yaml',
        epochs=100,
        imgsz=640,
        device=0,
        batch=16,
        patience=15,
        plots=False
    )
    print("Trening zakończony")



train_model()