import cv2
import pika
import requests
import numpy as np
import time


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="image_queue")

def callback(ch, method, properties, body):
    start = time.time()

    url = body.decode('utf-8')
    print(f"Odebrano URL: {url}")

    response = requests.get(url)
    arr = np.frombuffer(response.content, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    boxes, weights = hog.detectMultiScale(img)

    print({"people count": len(boxes)})

    print(f"Czas przetwarzania: {time.time() - start} sekund\n")

channel.basic_consume(queue="image_queue", on_message_callback=callback, auto_ack=True)
print("Oczekiwanie na wiadomości. Naciśnij CTRL+C, aby zakończyć.")
channel.start_consuming()