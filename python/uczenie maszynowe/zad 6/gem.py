import cv2
import numpy as np
from darknet import load_net_darknet, detect

# Załaduj model YOLO
model = load_net_darknet("yolov4.cfg", "yolov4.weights")

# Ustaw progi detekcji
confidence_threshold = 0.5
nms_threshold = 0.4

# Wczytaj dane obrazowe
image = cv2.imread("F:\samolot.jpg")

# Wykryj obiekty w obrazie
detections = detect(model, image, confidence_threshold, nms_threshold)

# Wyświetl wykryte obiekty na obrazie
for detection in detections:
    class_id, confidence, box = detection
    class_name = model.classes[class_id]

    x, y, w, h = box
    cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)
    cv2.putText(image, f"{class_name}: {confidence:.2f}", (int(x), int(y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Wyświetl obraz z naniesionymi obiektami
cv2.imshow("Image with detections", image)
cv2.waitKey(0)
