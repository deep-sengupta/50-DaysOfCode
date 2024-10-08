# Motion Detector
The program allows you to provide a video file and detects motion in the frames, highlighting movement with a rectangle and displaying the text "Status: Movement" on the video feed.

## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- Tkinter (comes pre-installed with Python)

You can install OpenCV using pip:
```
pip3 install opencv-python
```

## How to Run
- Run the Python script:
```
python3 main.py
```
- A window will appear where you can input the file path of the video you want to analyze for motion detection.
- Click the "Start" button to begin motion detection.
- The program will display the video with motion indicated by a green rectangle. You can exit the video feed by pressing the 'Esc' key.
- Click "Quit" to close the program.

## Error Handling
- If no video file path is provided or if the file cannot be opened, the application will display an error message.
- The video feed will stop automatically if the video ends or the 'Esc' key is pressed.