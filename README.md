# Professional Eye Landmark Extraction System
# 👁️ Eye Landmark Detection System

A real-time computer vision application that detects facial landmarks and extracts eye coordinates using **Python**, **OpenCV**, and **MediaPipe Face Mesh**. The system supports live webcam streams and can be extended for image and video processing, gaze estimation, blink detection, and eye-tracking applications.

---

## 🚀 Features

* Face Detection using MediaPipe Face Mesh
* Eye Landmark Extraction
* Real-Time Webcam Processing
* Left Eye Landmark Detection
* Right Eye Landmark Detection
* Multiple Face Support
* Landmark Visualization
* Modular Project Structure
* JSON Export Support
* Easy Integration with Gaze Tracking Systems

---

## 🛠️ Tech Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Programming Language      |
| OpenCV              | Image & Video Processing  |
| MediaPipe Face Mesh | Facial Landmark Detection |
| NumPy               | Numerical Operations      |
| JSON                | Data Export               |

---

## 📌 Eye Landmark Indices

### Left Eye

```python
LEFT_EYE = [33, 160, 158, 133, 153, 144]
```

### Right Eye

```python
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
```

These landmarks are extracted from MediaPipe's 468-point face mesh model.

---

## 📂 Project Structure

```text
Eye_Landmark_Detection/
│
├── src/
│   ├── eye_landmarks.py
│   ├── webcam_processor.py
│   ├── blink_detector.py
│   ├── gaze_estimator.py
│   └── utils.py
│
├── tests/
│   └── test_eye_landmarks.py
│
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Satyam104/Eye_Landmark_Detection.git

cd Eye_Landmark_Detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Webcam Mode

```bash
python main.py --mode webcam
```

The application will:

1. Open the webcam.
2. Detect faces in real time.
3. Extract eye landmarks.
4. Display eye landmark points on the screen.

Press **ESC** to exit.

---

## 📊 Sample Output

```json
{
    "left_eye": [
        [425,281],
        [429,275],
        [435,274],
        [445,282],
        [434,292],
        [427,291]
    ],
    "right_eye": [
        [598,284],
        [605,274],
        [613,275],
        [625,285],
        [614,295],
        [603,293]
    ]
}
```

---

## 🔄 Workflow

```text
Input Frame
      │
      ▼
MediaPipe Face Mesh
      │
      ▼
Face Landmark Detection
      │
      ▼
Eye Landmark Extraction
      │
      ▼
Coordinate Generation
      │
      ▼
Visualization & JSON Output
```

---

## 🧪 Test Cases

| Scenario              | Expected Result           |
| --------------------- | ------------------------- |
| Single Face           | Eye landmarks detected    |
| Multiple Faces        | All faces processed       |
| User with Glasses     | Eye landmarks extracted   |
| Moderate Head Tilt    | Stable landmark tracking  |
| Low Lighting          | Best-effort detection     |
| Partial Eye Occlusion | Partial landmark recovery |

---

## 🎯 Applications

* Eye Tracking Systems
* Gaze Estimation
* Blink Detection
* Driver Monitoring Systems
* Human-Computer Interaction
* Accessibility Tools
* Attention Monitoring

---

## 🔮 Future Enhancements

* Eye Aspect Ratio (EAR) Based Blink Detection
* Head Pose Estimation
* Gaze Direction Estimation
* CSV & JSON Export
* Streamlit Dashboard
* Real-Time Analytics
* Deep Learning-Based Eye Tracking

---

## 👨‍💻 Author

**Satyam Kumar**

B.Tech Computer Science Engineering

Amity University

GitHub: https://github.com/Satyam104

---

## 📜 License

This project is licensed under the MIT License.
