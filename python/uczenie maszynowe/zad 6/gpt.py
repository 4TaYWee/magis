import cv2
import numpy as np
import tensorflow as tf

# Wczytanie obrazu
image_path = 'F:\samolot.jpg'
image = cv2.imread(image_path)
image_height, image_width, _ = image.shape

# Wczytanie modelu YOLO
yolo_model = tf.keras.models.load_model("C:\\Users\\patry\\Desktop\\Praca dyplomowa\\python\\ultralytics-yolov5-915bbf2\\models\\yolo.py")

# Przygotowanie obrazu do detekcji
image_resized = cv2.resize(image, (416, 416)) # YOLO przyjmuje obrazy o rozmiarze 416x416
image_normalized = image_resized / 255.0
image_expanded = np.expand_dims(image_normalized, axis=0)

# Detekcja obiektów na obrazie
yolo_outputs = yolo_model.predict(image_expanded)
bounding_boxes, confidence_scores, class_ids = [], [], []
for output in yolo_outputs:
    boxes, scores, classes, _ = tf.image.combined_non_max_suppression(
        boxes=tf.reshape(output[:, :, :, 0:4], (tf.shape(output)[0], -1, 1, 4)),
        scores=tf.reshape(output[:, :, :, 4:], (tf.shape(output)[0], -1, tf.shape(output)[-1])),
        max_output_size_per_class=50,
        max_total_size=50,
        iou_threshold=0.5,
        score_threshold=0.5
    )
    bounding_boxes.append(boxes)
    confidence_scores.append(scores)
    class_ids.append(classes)

# Konwersja wyników na tablice NumPy
bounding_boxes = [box.numpy() for box in bounding_boxes]
confidence_scores = [score.numpy() for score in confidence_scores]
class_ids = [class_id.numpy() for class_id in class_ids]

# Wyświetlenie wyników na obrazie
for box, score, class_id in zip(bounding_boxes[0], confidence_scores[0], class_ids[0]):
    if score > 0.5: # Wyświetl tylko detekcje z pewnością powyżej 0.5
        xmin, ymin, xmax, ymax = box
        xmin = int(xmin * image_width)
        ymin = int(ymin * image_height)
        xmax = int(xmax * image_width)
        ymax = int(ymax * image_height)
        class_name = 'Object'  # Możesz tutaj użyć etykiet klasyfikatora, aby określić nazwę wykrytego obiektu
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(image, f'{class_name} {score:.2f}', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Wyświetlenie obrazu z detekcjami
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
