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

## 🛠️ Requirements

Install all necessary Python libraries:

```bash
pip install opencv-python dlib numpy pillow keyboard
```

You also need:
- A functional **webcam**
- The pretrained shape predictor model file:  
  👉 [Download here (68 landmarks)](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)

> Extract the `.bz2` file to get `shape_predictor_68_face_landmarks.dat` and place it in the same folder as the script.

---

## 🧠 Pretrained Model

This script **reuses a pretrained face landmark detection model** provided by the [dlib project](https://github.com/davisking/dlib-models). Specifically, it uses:

📁 `shape_predictor_68_face_landmarks.dat`  
🔗 [Download Link](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)

---

## 🚀 How It Works

1. Launches the webcam and begins capturing frames.
2. Detects faces using dlib’s frontal detector.
3. Identifies key facial landmarks:
   - Point **27**: Top of the nose bridge
   - Point **30**: Tip of the nose
4. Calculates the angle of tilt using:
   ```python
   angle = math.degrees(math.atan(abs(x1 - x2) / abs(y1 - y2)))
   ```
5. Determines head direction:
   - Tilt **Left** → `x1 > x2` → 🔊 Volume Up
   - Tilt **Right** → `x1 < x2` → 🔉 Volume Down
   - Small angle → No significant motion
6. Annotates direction on the video frame.


## 🌱 Future Scope

This project is a foundation for hands-free interaction using face gestures.

**Current Implementation**:
- Triggers **volume control** using head movement.

**Can Be Extended To**:
- Trigger any custom action or event:
  - Page navigation (Left/Right)
  - Media control (Play/Pause)
  - Accessibility tools
  - IoT/Smart Home device control
  - Game interactions

---

## 🧪 Troubleshooting

- Ensure good lighting for accurate detection.
- Avoid occlusions (e.g., glasses or masks).
- If `keyboard` doesn't work, try running the script as administrator.
- Verify the webcam has permission to be accessed by the script.

---

## 📜 License

This project is intended for educational and research purposes. Feel free to modify or integrate it into larger systems.
