import cv2
import torch
from ultralytics import YOLO
import time

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class ObjectDetection:
    def __init__(self, model_path='yolov8n.pt', source=0, display_fps=True):
        self.model = YOLO(model_path).to(device)
        self.capture = cv2.VideoCapture(source)
        self.display_fps = display_fps
        if not self.capture.isOpened():
            raise Exception("Error: Could not open video capture device")

    def _draw_detections(self, frame, results):
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
                label_id = int(box.cls[0].item())
                confidence = box.conf[0].item()
                class_label = self.model.names[label_id]
                label_text = f"{class_label}: {confidence:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        return frame

    def _display_fps(self, frame, fps):
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        return frame

    def process_frame(self, frame):
        start_time = time.time()
        results = self.model(frame)
        frame = self._draw_detections(frame, results)
        if self.display_fps:
            fps = 1.0 / (time.time() - start_time)
            frame = self._display_fps(frame, fps)
        return frame

    def run(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            processed_frame = self.process_frame(frame)
            cv2.imshow('Advanced Object Detection', processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detection = ObjectDetection(model_path='yolov8n.pt', source=0, display_fps=True)
    detection.run()