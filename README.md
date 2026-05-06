# Hand-Gesture-Detection
This is a project about the virtual hand gesture detection  
#  Hand Gesture Virtual Mouse

A computer vision-based system that allows users to control mouse operations using hand gestures in real-time. This project uses **MediaPipe**, **OpenCV**, and **Python** to enable touchless human-computer interaction.

---

##  Features

*  Cursor Movement using Index Finger
*  Left Click (Thumb + Index)
*  Right Click (Thumb + Middle)
*  Scroll (Index + Middle - vertical movement)
*  Smooth and responsive cursor control
*  Gesture conflict handling for better accuracy
*  Interactive UI with HUD overlay

---

##  Tech Stack

* **Frontend**: HTML, Tailwind CSS
* **Backend**: Python (Flask)
* **Computer Vision**: OpenCV, MediaPipe
* **Automation**: PyAutoGUI

---

##  Project Structure

```
Hand-Gesture/
│
├── app.py                  # Flask app
├── gesture_controller.py   # Gesture logic
├── hand_tracking.py        # Hand detection (MediaPipe)
├── templates/
│   └── index.html          # UI
├── requirements.txt
└── README.md
```

---

##  Installation (Local Setup)

```bash
git clone <your-repo-link>
cd Hand-Gesture

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

---

## ▶ Usage

1. Allow webcam access
2. Use gestures to control your mouse

---

##  Gesture Controls

| Gesture           | Action      |
| ----------------- | ----------- |
|  Index Finger   | Move Cursor |
| Thumb + Index           | Left Click  |
| Thumb +  Middle   | Right Click |
| ✌️ + Move Up/Down | Scroll      |

---

##  Deployment

###  Note:

This project **cannot be fully deployed on cloud platforms** like Render or Hugging Face because:

*  Requires system mouse control (`pyautogui`)
*  Requires direct webcam access (`cv2.VideoCapture`)

###  Alternative:

A **Gradio-based version** can be deployed on Hugging Face for gesture visualization.

---

## Download & Run (No Installation Required)

> Don't want to set up Python or install dependencies? Just download and run the ready-to-use **Windows executable (`.exe`)** directly!

### Download the Application

| Platform | Link |
|----------|------|
| Windows (64-bit) | [**Download VirtualMouse.exe**](https://drive.google.com/file/d/1BSXhG573yXX0EnbiZhggybb6l796bNki/view) |

### How to Run

1. **Download** the `.exe` file from the link above.
2. **Double-click** the downloaded `VirtualMouse.exe` to launch the application.
3. When prompted, **allow webcam access** so the app can detect your hand gestures.
4. Your cursor is now controlled by your hand! Use the gestures listed in the **Gesture Controls** table below.
5. To **exit**, press `Q` on your keyboard or close the application window.

### Windows SmartScreen Warning

When you run the `.exe` for the first time, Windows may show a **"Windows protected your PC"** warning. This is normal for unsigned applications. To proceed:

1. Click **"More info"**
2. Click **"Run anyway"**

The application is completely safe and open-source.

### System Requirements

| Requirement | Details |
|-------------|---------|
| **OS** | Windows 10 / 11 (64-bit) |
| **Webcam** | Built-in or external USB webcam |
| **RAM** | Minimum 4 GB recommended |
| **Lighting** | Good ambient lighting for accurate gesture detection |
| **Python** | ❌ Not required — everything is bundled in the `.exe` |

---

##  Limitations

* Requires good lighting conditions
* Works best with a single hand
* System-level mouse control only works locally
* Gesture accuracy depends on camera quality

---

##  Future Enhancements

*  Drag & Drop gesture
*  AI-based gesture recognition
*  Gesture customization
*  Fully browser-based implementation
*  Mobile compatibility

---

##  Applications

* Touchless systems
* Accessibility tools
* Smart environments
* AR/VR interaction

---

##  Author

**Kavya Saxena**

---

##  Acknowledgment

* MediaPipe by Google
* OpenCV community

---

##  Description (Short)

A real-time hand gesture-based virtual mouse system built using MediaPipe and OpenCV, enabling touchless interaction with a computer.

---
