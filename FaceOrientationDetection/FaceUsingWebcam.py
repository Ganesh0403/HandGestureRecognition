# We Import the necessary packages needed 
import cv2 
import numpy as np 
import dlib 
from PIL import Image
import math
from keyboard import Keyboard

# We initialise detector of dlib 
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
 

vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
 
# Start the main program 
while True: 
    _, frame = vid.read()
    img_resp = cv2.resize(frame, (96,64))    
    # We actually Convert to grayscale conversion 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = detector(gray) 
    for face in faces: 
        # The face landmarks code begins from here 
        landmarks = predictor(gray, face) 
        # We are then accesing the landmark points  
        # for n in range(0, 68):
        x1 = landmarks.part(27).x 
        y1 = landmarks.part(27).y
        x2 = landmarks.part(30).x 
        y2 = landmarks.part(30).y 
        cv2.circle(frame, (x1, y1), 2, (255, 255, 0), -1)
        cv2.circle(frame, (x2, y2), 2, (255, 255, 0), -1)

        result_text = str(int(math.degrees(math.atan(abs(x1-x2)/abs(y1-y2)))))
        deg = int(math.degrees(math.atan(abs(x1-x2)/abs(y1-y2))))
        if deg>10 and x1>x2:
            result_text += "  Left"
            Keyboard.key(Keyboard.VK_VOLUME_UP)
        elif x1<x2 and deg>10:
            result_text += " Right"
            Keyboard.key(Keyboard.VK_VOLUME_DOWN)
        else:
            result_text += "  No Motion"
        cv2.putText(frame,result_text,(200,100),cv2.FONT_HERSHEY_DUPLEX,
              fontScale = 2,
              color = (0,0,0),thickness=2)

    cv2.imshow("Frame", frame) 
    key = cv2.waitKey(1) 
    if key == 27: 
        break # press esc the frame is destroyed
