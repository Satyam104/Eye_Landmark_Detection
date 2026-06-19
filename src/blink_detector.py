import math

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def eye_aspect_ratio(eye):
    A=distance(eye[1],eye[5])
    B=distance(eye[2],eye[4])
    C=distance(eye[0],eye[3])
    return (A+B)/(2.0*C+1e-6)
