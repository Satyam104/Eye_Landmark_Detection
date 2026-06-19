import cv2, mediapipe as mp
from mediapipe.python.solutions import face_mesh
LEFT_EYE=[33,160,158,133,153,144]
RIGHT_EYE=[362,385,387,263,373,380]

class EyeLandmarkExtractor:
    def __init__(self):
        self.mesh = face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=10,
            refine_landmarks=True)

    def extract(self,frame):
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.mesh.process(rgb)
        faces=[]
        if results.multi_face_landmarks:
            h,w,_=frame.shape
            for face in results.multi_face_landmarks:
                left=[[int(face.landmark[i].x*w),int(face.landmark[i].y*h)] for i in LEFT_EYE]
                right=[[int(face.landmark[i].x*w),int(face.landmark[i].y*h)] for i in RIGHT_EYE]
                faces.append({"left_eye":left,"right_eye":right})
        return faces
