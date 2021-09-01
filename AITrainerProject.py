import time

import cv2 as cv
import numpy as np
import PoseModule as pm

import tkinter as tk
from tkinter import ttk

# choose workout
def click(x):
    global flag
    win.destroy()
    flag = x


win = tk.Tk()
win.title("AI Trainer")
Lbl = ttk.Label(win, text="Choose your workout")
Lbl.pack()
flag = ""

action1 = ttk.Button(win, text="Bicep Curl", command=lambda: click("Bicep Curl"))
action2 = ttk.Button(win, text="Squat", command=lambda: click("Squat"))
action1.pack()
action2.pack()

win.mainloop()


def detect_bicep_curls():
    global per, bar
    # left arm
    angle = detector.get_angle(img, 11, 13, 15, draw=True)
    # right arm
    detector.get_angle(img, 12, 14, 16, draw=True)
    per = np.interp(angle, (50, 160), (100, 0))
    bar = np.interp(angle, (50, 160), (300, 600))


def detect_squats():
    global per, bar
    # left side
    angle = detector.get_angle(img, 11, 23, 25, draw=True)
    per = np.interp(angle, (65, 165), (100, 0))
    bar = np.interp(angle, (65, 165), (300, 600))

cap = cv.VideoCapture(0)
fps = cap.get(cv.CAP_PROP_FPS)
delay = round(1000 / fps)

detector = pm.PoseDetector()
count = 0
direction = 0
sec = 5

while cap.isOpened():

    #countdown before it starts
    prev = time.time()
    while sec > 0:
        ret, img = cap.read()
        cv.putText(img, str(sec), (img.shape[1]//2, img.shape[0]//2), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 5)
        cv.imshow("image", img)
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            sec -= 1
        cv.waitKey(1)

    # detect workout
    ret, img = cap.read()

    if not ret:
        break

    img = detector.get_pose(img, False)
    lmList = detector.get_position(img,False)

    if len(lmList) != 0:
        if flag == "Bicep Curl":
            detect_bicep_curls()
        elif flag == "Squat":
            detect_squats()

        # counting reps
        color = (255,255,0)
        if per == 100:
            color = (0, 0, 255)
            if direction == 0:
                count += 0.5
                direction = 1
        if per == 0:
            color = (0, 0, 255)
            if direction == 1:
                count += 0.5
                direction = 0
        cv.putText(img, str(int(count)), (50,100), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)

        cv.rectangle(img, (50, 300), (150,600),(255,255,255),cv.FILLED)
        cv.rectangle(img, (50, int(bar)), (150,600),color,cv.FILLED)
        cv.putText(img, f'{int(per)}%', (50,280), cv.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv.imshow("image", img)

    if cv.waitKey(1) == 27:
        break
