import argparse
from src.webcam_processor import start_webcam

parser=argparse.ArgumentParser()
parser.add_argument("--mode",default="webcam")
args=parser.parse_args()

if args.mode=="webcam":
    start_webcam()
