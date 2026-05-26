# AI-Based Autonomous Emergency Braking with Obstacle Classification

## Overview
This project implements an **AI-based Autonomous Emergency Braking (AEB) system** that detects obstacles using computer vision and triggers an emergency braking simulation when a potential collision is detected.

The system captures real-time video from a camera and processes the frames using a **MobileNet-SSD deep learning model** for object detection. It identifies objects such as pedestrians, vehicles, bicycles, and other obstacles in front of the vehicle.

After detecting objects, the system performs **distance estimation, Time-to-Collision (TTC) calculation, trajectory prediction, and risk assessment**. When a high-risk situation is detected, the system triggers a braking warning, records the event video, and logs the incident to a **Firebase cloud database**.

This project demonstrates how **Artificial Intelligence, Computer Vision, and IoT technologies** can be integrated to build a prototype **Advanced Driver Assistance System (ADAS)**.

---

# Features
- Real-time object detection using **MobileNet-SSD**
- Obstacle classification (person, car, bus, bicycle, etc.)
- Object tracking
- Distance estimation
- Time-to-Collision (TTC) calculation
- Trajectory prediction
- Risk level prediction
- Emergency braking simulation
- Event video recording
- Cloud logging using **Firebase**
- FPS monitoring

---

# System Architecture
```
Camera Input
     ↓
Object Detection (MobileNet-SSD)
     ↓
Object Classification
     ↓
Object Tracking
     ↓
Distance Estimation
     ↓
Time-to-Collision Calculation
     ↓
Trajectory Prediction
     ↓
Risk Prediction
     ↓
Emergency Brake Activation
     ↓
Event Video Recording
     ↓
Cloud Logging (Firebase)
```

---

# Hardware Requirements
- Raspberry Pi 5 (for deployment)
- USB Camera
- Servo Motor (Brake actuator simulation)
- MicroSD Card
- Laptop / PC for development

---

# Software Requirements
- Python 3.x
- OpenCV
- NumPy
- TensorFlow / Deep Learning Model
- Firebase Admin SDK
- Visual Studio Code / Python IDE

---

# Project Structure
```
ai-autonomous-braking-system
│
├── models
│   ├── MobileNetSSD_deploy.caffemodel
│   └── MobileNetSSD_deploy.prototxt
│
├── scripts
│   ├── object_detection.py
│   ├── distance_estimation.py
│   ├── risk_prediction.py
│   ├── trajectory_prediction.py
│   ├── sort_tracker.py
│   ├── event_recorder.py
│   └── cloud_logger.py
│
├── requirements.txt
├── test_model.py
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/CharanReddy2607/ai-autonomous-braking-system.git
cd ai-autonomous-braking-system
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Run the Project

```
python scripts/object_detection.py
```

The system will start the camera and begin detecting obstacles in real time.

---

# Example Output
```
person ID:3 1.2m TTC:0.24s APPROACHING HIGH
```

If a high collision risk is detected:

- Emergency brake warning is displayed
- Alert sound is triggered
- Event video is recorded
- Incident is logged to Firebase

---

# Applications
- Autonomous Vehicles
- Advanced Driver Assistance Systems (ADAS)
- Collision Avoidance Systems
- Smart Transportation
- Robotics Safety Systems

---

# Limitations
- Distance estimation using a single camera is approximate
- Performance may decrease under poor lighting conditions
- FPS may vary depending on system hardware

---

# Future Improvements
- Integration with **Radar or LiDAR sensors**
- GPU acceleration for higher FPS
- Steering-based collision avoidance
- Multi-camera perception system
- AI-based risk scoring models

---

# References
- MobileNet: Efficient Convolutional Neural Networks for Mobile Vision Applications  
- SSD: Single Shot MultiBox Detector  
- OpenCV Documentation  
- Firebase Cloud Database Documentation  

---

# Author

**Burramukku Madhu Charan Reddy**  
B.Tech Computer Science Engineering  
KL University  

GitHub:  
https://github.com/CharanReddy2607
