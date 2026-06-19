import cv2
from .eye_landmarks import EyeLandmarkExtractor
from .utils import draw_eye_landmarks

def start_webcam():
    cap=cv2.VideoCapture(0)
    extractor=EyeLandmarkExtractor()
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        data=extractor.extract(frame)
        draw_eye_landmarks(frame,data)
        cv2.imshow("Professional Eye Tracker",frame)
        if cv2.waitKey(1)&0xFF==27:
            break
    cap.release()
    cv2.destroyAllWindows()
