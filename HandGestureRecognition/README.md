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

## 🏗️ System Architecture

### Model Architecture
- **3D ResNet**: Convolutional neural network that processes both spatial and temporal features
- **Input**: 16-frame sequences of 64x96 RGB images
- **Output**: 27 gesture classes
- **Framework**: Keras/TensorFlow

### Key Components
- `Train.ipynb` - Model training notebook
- `Classification.ipynb` - Real-time inference system
- `Lib/resnet_model.py` - 3D ResNet implementation
- `Lib/data_loader.py` - Data preprocessing and loading
- `Lib/utils.py` - Utility functions
- `keyboard.py` - System keyboard control interface

---

## 🎯 Supported Gestures

The system recognizes 27 different hand gestures, including:

- **Directional Swipes**: Left, Right, Up, Down
- **Two-Finger Slides**: Left, Right sliding motions  
- **Push Gestures**: Hand pushing away/toward camera
- **Media Controls**: Gesture-to-keyboard mapping for media playback
- **Volume Controls**: Gesture-based volume adjustment

---

## 🛠️ Requirements

### Python Dependencies
```bash
pip install tensorflow keras opencv-python numpy pandas
```

### Hardware Requirements
- **Webcam**: For real-time gesture capture
- **GPU** (recommended): For faster model training and inference
- **RAM**: At least 8GB for model training

### Model Files
- Trained model: `resnetmodel.hdf5`
- Labels file: `jester-v1-labels.csv`

---

## 🚀 Usage

### Training a New Model

1. **Prepare Dataset**: Organize gesture videos in appropriate format
2. **Configure Parameters**: 
   ```python
   target_size = (64,96)
   nb_frames = 16
   nb_classes = 27
   batch_size = 64
   ```
3. **Run Training**: Execute `Train.ipynb`
4. **Monitor Progress**: Check training graphs in `graphs/` folder

### Real-time Classification

1. **Load Model**: 
   ```python
   model = load_model("resnetmodel.hdf5")
   ```
2. **Start Webcam**: Run `Classification.ipynb`
3. **Perform Gestures**: The system will recognize gestures and trigger actions

### Gesture-to-Action Mapping

- **Swipe Left** → Previous Track
- **Swipe Right** → Next Track  
- **Swipe Up** → Volume Up
- **Swipe Down** → Volume Down
- **Two-Finger Slide Left** → Previous Track
- **Two-Finger Slide Right** → Next Track

---

## 📊 Model Performance

### Training Configuration
- **Optimizer**: SGD with custom learning rate
- **Architecture**: 3D ResNet with batch normalization
- **Data Augmentation**: Frame sampling and resizing
- **Validation**: Cross-validation on gesture dataset

### Performance Metrics
- Training accuracy and loss graphs available in `graphs/` folder
- Real-time inference: ~30 FPS on modern hardware
- Model size: Optimized for real-time performance

---

## 📁 Directory Structure

```
HandGestureRecognition/
├── Train.ipynb              # Model training notebook
├── Classification.ipynb     # Real-time inference
├── keyboard.py             # Keyboard control interface
├── FlowChart.jpeg          # System architecture diagram
├── Lib/                    # Core libraries
│   ├── resnet_model.py     # 3D ResNet implementation
│   ├── data_loader.py      # Data preprocessing
│   ├── utils.py            # Utility functions
│   └── image.py            # Image processing utilities
└── graphs/                 # Training performance graphs
    ├── 16 acc.jpg         # Accuracy progression
    └── 16 loss.jpg        # Loss progression
```

---

## 🔬 Technical Details

### Data Processing
- **Frame Sampling**: 16 consecutive frames per gesture sequence
- **Preprocessing**: Normalization to [0,1] range
- **Augmentation**: Temporal and spatial variations

### Model Training
- **Loss Function**: Categorical cross-entropy
- **Regularization**: L2 regularization and dropout
- **Optimization**: SGD with momentum
- **Callbacks**: Model checkpointing for best weights

### Real-time Pipeline
1. **Frame Capture**: Webcam input at 500x500 resolution
2. **Preprocessing**: Resize to 96x64, normalize
3. **Buffer Management**: Maintain 16-frame sliding window
4. **Prediction**: Model inference every 16 frames
5. **Action Trigger**: Execute corresponding keyboard action

---

## 🎮 Customization

### Adding New Gestures
1. Collect gesture video data
2. Update label mappings in dataset
3. Retrain model with new gesture classes
4. Update action mappings in `Classification.ipynb`

### Modifying Actions
Edit the gesture-to-action mapping in the classification loop:
```python
if(predicted_value == gesture_id):
    final_label = "Custom Gesture"
    Keyboard.key(Keyboard.VK_CUSTOM_ACTION)
```

---

## 🐛 Troubleshooting

### Common Issues
- **Model Loading Error**: Ensure model file path is correct
- **Webcam Access**: Check camera permissions and availability
- **Performance Issues**: Reduce frame rate or model complexity
- **Gesture Recognition**: Ensure good lighting and clear hand visibility

### Performance Optimization
- Use GPU acceleration for faster inference
- Adjust buffer size for responsiveness vs. accuracy trade-off
- Optimize model architecture for deployment constraints

---

## 📚 References

- 3D ResNet Architecture: [Keras ResNet3D](https://github.com/JihongJu/keras-resnet3d/)
- Original 2D ResNet: [Keras ResNet](https://github.com/raghakot/keras-resnet)
- Gesture Dataset: Jester Dataset format
- System Integration: Windows Keyboard API

---

## 📜 License

This project is intended for educational and research purposes. The 3D ResNet implementation is based on existing open-source implementations with appropriate attribution. 