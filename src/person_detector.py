from ultralytics import YOLO
import numpy as np

class PersonDetector:
    def __init__(self, model_path="yolov8n.pt", conf=0.3):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        res = self.model.predict(frame, conf=self.conf, verbose=False)[0]
        people = []
        for b in res.boxes:
            if int(b.cls[0]) == 0:
                x1, y1, x2, y2 = b.xyxy[0].tolist()
                people.append({"bbox": [x1, y1, x2, y2],
                               "center": [(x1+x2)/2, (y1+y2)/2],
                               "conf": float(b.conf[0])})
        return people
