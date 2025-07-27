# 🤲 Hand Gesture Recognition Using 3D ResNet

This section implements a sophisticated hand gesture recognition system using deep learning. The system uses a 3D ResNet architecture to classify hand gestures from video sequences and trigger corresponding keyboard actions in real-time.

---

## 📌 Features

- **Deep Learning Model**: 3D ResNet architecture for temporal gesture recognition
- **Real-time Classification**: Live webcam-based gesture recognition
- **27 Gesture Classes**: Supports various hand gestures including swipes, slides, and pushes
- **Keyboard Integration**: Automatically triggers system actions based on recognized gestures
- **Training Pipeline**: Complete model training and evaluation system
- **Performance Visualization**: Training accuracy and loss graphs

---
## Video
![Demo](Videos/27_Gesture_Recognition_VIDEO.mp4)

---

# 🎥 Face Orientation Detection via Webcam

This Python script detects face orientation in real-time using a webcam. Based on the detected direction of the user's head tilt, it can trigger system-level events — such as adjusting volume — using the keyboard.

---

## 📌 Features

- Real-time facial landmark detection using webcam input.
- Uses pretrained dlib model to extract facial landmarks.
- Calculates head tilt direction (Left, Right, or No Motion).
- Triggers keyboard actions based on direction:
  - **Left tilt** → Volume Up
  - **Right tilt** → Volume Down
- Annotated live feed shows head direction and tracking points.

---
## Video
![Demo](Videos/Face_Left_Right_Recognition_VIDEO.mp4)
---