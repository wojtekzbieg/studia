import cv2
import pika
import requests
import numpy as np
import time
import json
import os

rabbit_host = os.getenv("RABBITMQ_HOST", "localhost")
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_host))
channel = connection.channel()
channel.queue_declare(queue="image_queue")

def callback(ch, method, properties, body):
    start = time.time()

    decoded_body = body.decode('utf-8')
    body_dict = json.loads(decoded_body)

    img_url = body_dict["img_url"]
    id = body_dict["id"]

    response = requests.get(img_url)
    arr = np.frombuffer(response.content, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    boxes, weights = hog.detectMultiScale(img)

    liczba_ludzi = len(boxes)
    czas_przetwarzania = time.time() - start

    wyniki = {"id": id, "liczba_ludzi": liczba_ludzi, "czas_przetwarzania": czas_przetwarzania, "img_url": img_url}

    api_host = os.getenv("API_HOST", "127.0.0.1")
    endpoint_url = f"http://{api_host}:8000/submit_img_analysis_results"

    requests.post(url=endpoint_url,json=wyniki)

    print(wyniki)
    print()

channel.basic_consume(queue="image_queue", on_message_callback=callback, auto_ack=True)
print("Oczekiwanie na wiadomości. Naciśnij CTRL+C, aby zakończyć.")
channel.start_consuming()