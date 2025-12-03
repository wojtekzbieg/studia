import cv2
import pika
import requests
import numpy as np
import time
import json


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="image_queue")

def callback(ch, method, properties, body):
    start = time.time()

    decoded_body = body.decode('utf-8')
    body_dict = json.loads(decoded_body)

    url = body_dict["img_url"]
    id = body_dict["id"]

    # print(f"Odebrano URL: {url}")

    response = requests.get(url)
    arr = np.frombuffer(response.content, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    boxes, weights = hog.detectMultiScale(img)

    liczba_ludzi = len(boxes)
    czas_przetwarzania = time.time() - start

    print({"id": id, "liczba ludzi": liczba_ludzi, "czas przetwarzania": czas_przetwarzania, "url": url})
    print()

channel.basic_consume(queue="image_queue", on_message_callback=callback, auto_ack=True)
print("Oczekiwanie na wiadomości. Naciśnij CTRL+C, aby zakończyć.")
channel.start_consuming()