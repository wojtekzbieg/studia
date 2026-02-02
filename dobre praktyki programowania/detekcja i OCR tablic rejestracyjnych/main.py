import xml.etree.ElementTree as ET
import cv2
import easyocr
import time
import os
from ultralytics import YOLO


reader = easyocr.Reader(['pl'], gpu=True)
MODEL_PATH = 'runs/detect/train/weights/best.pt'
IMAGES_DIR = 'photos'

def zaladuj_slownik_tablic():
    tree = ET.parse("annotations.xml")
    root = tree.getroot()

    slownik = {}
    for img in root.findall("image"):
        num_rej = img.find("box/attribute").text
        slownik[img.get("name")] = num_rej

    return slownik

def calculate_final_grade(accuracy_percent, processing_time_sec):
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0

    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2

def levenshtein_dist(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_dist(s2, s1)
    if not s2:
        return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            ins, dele = prev[j + 1] + 1, curr[j] + 1
            sub = prev[j] + (c1 != c2)
            curr.append(min(ins, dele, sub))
        prev = curr
    return prev[-1]

def fix_text(text):
    if not text:
        return ""
    text = ''.join(e for e in text if e.isalnum()).upper()

    replacements = {' ': '', '.': '', '-': '', ':': '', '|': '1', '/': '1', '\\': '1', '(': 'C', ')': 'J'}
    for k, v in replacements.items(): text = text.replace(k, v)

    if len(text) < 4:
        return ""
    chars = list(text)
    length = len(chars)

    for i in range(min(2, length)):
        if chars[i] in ['0','Q']: chars[i] = 'O'
        if chars[i] == '1': chars[i] = 'I'
        if chars[i] == '2': chars[i] = 'Z'
        if chars[i] == '4': chars[i] = 'A'
        if chars[i] in ['5','6']: chars[i] = 'S'
        if chars[i] == '8': chars[i] = 'B'

    return "".join(chars)

def preprocess_image(img):
    if img is None or img.size == 0:
        return None
    h, w = img.shape[:2]

    img = img[:, int(w * 0.13):]

    img = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    return gray

def main():
    model = YOLO(MODEL_PATH)

    truth_data = zaladuj_slownik_tablic()
    images = [f for f in os.listdir(IMAGES_DIR) if f in truth_data][:100]

    print(f"Start testu")
    correct = 0
    start = time.time()

    for i, filename in enumerate(images):
        full_path = os.path.join(IMAGES_DIR, filename)
        img_orig = cv2.imread(full_path)
        if img_orig is None:
            continue

        results = model.predict(img_orig, conf=0.10, verbose=False, device=0)
        plate_crop = None

        if results[0].boxes:
            boxes = sorted(results[0].boxes, key=lambda x: x.conf[0], reverse=True)
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w_box = x2 - x1
                h_box = y2 - y1
                aspect = w_box / float(h_box)

                if 2.0 < aspect < 6.0:
                    pad_x = int((x2 - x1) * 0.05)
                    nx1 = max(0, x1 - pad_x)
                    nx2 = min(img_orig.shape[1], x2 + pad_x)
                    plate_crop = img_orig[y1:y2, nx1:nx2]
                    break

        if plate_crop is None:
            h, w = img_orig.shape[:2]
            plate_crop = img_orig[int(h*0.4):int(h*0.7), int(w*0.2):int(w*0.8)]

        processed = preprocess_image(plate_crop)
        detected = ""

        try:
            ocr_results = reader.readtext(processed, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        except:
            ocr_results = []

        best_height = 0
        if ocr_results:
            for res in ocr_results:
                coords = res[0]
                text_raw = res[1]
                conf = res[2]
                text_height = abs(coords[3][1] - coords[0][1])

                text_clean = fix_text(text_raw)

                if len(text_clean) < 4 or len(text_clean) > 9:
                    continue

                if text_height > best_height and conf > 0.2:
                    best_height = text_height
                    detected = text_clean

        truth = truth_data.get(filename)

        is_ok = False
        dist = levenshtein_dist(detected, truth)

        if dist <= 0:
            is_ok = True

        if is_ok:
            correct += 1

        icon = '✅' if is_ok else '❌'
        print(f"[{i+1:3}] {icon} Odczyt: {detected:10} | Prawda: {truth:10} (Błędy: {dist})")

    total_time = time.time() - start
    acc = (correct / len(images)) * 100

    print("-" * 30)
    print(f"Poprawnie: {correct}/{len(images)}")
    print(f"Czas: {total_time:.2f} s")
    print(f"Ocena: {calculate_final_grade(acc, total_time)}")

main()