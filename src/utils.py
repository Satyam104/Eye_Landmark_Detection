import cv2,json

def draw_eye_landmarks(frame,data):
    for face in data:
        for p in face["left_eye"]+face["right_eye"]:
            cv2.circle(frame,tuple(p),2,(0,255,0),-1)
    return frame

def export_json(data,path):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
