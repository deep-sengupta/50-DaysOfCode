import cv2
import tkinter as tk
from tkinter import messagebox

def quit_program():
    global running
    running = False
    root.quit()

def start_motion_detection():
    global running
    file_path = entry.get()
    if not file_path:
        messagebox.showwarning("Input Error", "Please provide a valid video file path.")
        return

    cap = cv2.VideoCapture(file_path)

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened() and running:
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dialated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 1000:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: Movement", (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

        resized_frame = cv2.resize(frame1, (640, 480))
        cv2.imshow("Live Feed", resized_frame)
        frame1 = frame2
        ret, frame2 = cap.read()

        if not ret or cv2.waitKey(40) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Motion Detection Setup")
root.geometry("400x250")

heading = tk.Label(root, text="Motion Detector", font=('Arial', 24, 'bold'), pady=20)
heading.pack()

entry_label = tk.Label(root, text="Enter Video File Path:", font=('Arial', 14))
entry_label.pack(pady=10)
entry = tk.Entry(root, width=50, font=('Arial', 12))
entry.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_motion_detection, font=('Arial', 14), width=12)
start_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_program, font=('Arial', 14), width=12)
quit_button.pack(pady=10)

running = True
root.mainloop()