import math

import cv2 as cv
import mediapipe as mp


class PoseDetector:

    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

    def get_pose(self, img, draw=True):
        # if not realtime
        # imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # self.results = self.pose.process(imgRGB)

        #if realtime
        self.results = self.pose.process(img)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def get_position(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 15, (255,0,0), 5)
        return self.lmList

    def get_angle(self,img, p1, p2, p3, draw=True):

        # get the landmarks
        _, x1, y1 = self.lmList[p1]
        _, x2, y2 = self.lmList[p2]
        _, x3, y3 = self.lmList[p3]

        # find the angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
        
        # 0 <= angle <= 180
        if angle < 0:
            angle += 360
        if angle > 180:
            angle = 360 - angle
        # draw
        if draw:
            cv.line(img, (x1, y1), (x2, y2), (255,255,255),3)
            cv.line(img, (x3, y3), (x2, y2), (255,255,255),3)

            cv.circle(img, (x1, y1), 15, (255, 0, 0), 5)
            cv.circle(img, (x2, y2), 15, (255, 0, 0), 5)
            cv.circle(img, (x3, y3), 15, (255, 0, 0), 5)

            cv.putText(img, str(int(angle)), (x2-20, y2+50), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 2)

        return angle
