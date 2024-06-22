import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained YOLOv3 model
yolo_model = load_model('yolov3.h5')

# Define function to detect traffic signs
def detect_traffic_signs(image):
    # Preprocess image
    image = cv2.resize(image, (416, 416))
    image = image / 255.0

    # Run YOLOv3 model
    outputs = yolo_model.predict(image)

    # Get bounding box coordinates
    scores = outputs[0][:, 5:]
    class_ids = np.argmax(scores, axis=1)
    confidences = scores[np.arange(len(scores)), class_ids]
    boxes = outputs[1]

    # Filter out weak detections
    confidence_threshold = 0.5
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.4)

    # Draw bounding box around detected traffic sign
    for i in indices:
        x, y, w, h = boxes[i]
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image