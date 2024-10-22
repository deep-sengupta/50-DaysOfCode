# Advanced Real-Time Object Detection using YOLOv8 and OpenCV
This project is a Python-based real-time object detection system utilizing the YOLOv8 model from the `ultralytics` library and OpenCV for video processing. The program captures live video, detects objects in real-time, and displays bounding boxes around detected objects along with their labels and confidence scores. Additionally, the system tracks and displays the frame rate (FPS) to monitor performance.

## Requirements
Ensure you have the following dependencies installed before running the project:

- Python 3.x
- torch (CUDA is optional but recommended for faster inference)
- ultralytics (for YOLO model loading)
- OpenCV (for video capture and image display)

```
pip install torch torchvision torchaudio
pip install ultralytics
pip install opencv-python
```

## Usage
Once the script is running, it will open a video window displaying the webcam feed (or selected video source) with real-time object detection overlays. Bounding boxes, object labels, and confidence scores are displayed for each detected object.<br><br>
Press `q` to exit the program.