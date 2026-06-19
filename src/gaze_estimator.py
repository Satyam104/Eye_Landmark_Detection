def estimate_gaze(left_eye,right_eye):
    cx=sum([p[0] for p in left_eye])/len(left_eye)
    if cx<250:
        return "LEFT"
    elif cx>450:
        return "RIGHT"
    return "CENTER"
