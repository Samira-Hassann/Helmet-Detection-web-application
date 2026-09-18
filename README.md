# ⛑️ Helmet & Safety Gear Detection (YOLO11m)

An end-to-end Computer Vision system that detects safety helmets and unprotected heads in real time for industrial safety environments using **YOLO11** and **Streamlit**.

🚀 **Live Demo:** [Helmet Detection Web App](https://helmet-detection-web-application.streamlit.app/)  
📌 **Kaggle Notebook:** [Helmet & Safety Gear Detection (YOLO11)](https://www.kaggle.com/code/samoura/mask-detection)

## 📊 Dataset Overview
- **Source:** Roboflow Universe (`hardhat-b12dh`)
- **Classes:**
  - `head`: Unprotected head
  - `helmet`: Head wearing a safety helmet
- **Splits:** 2,739 Train | 782 Valid | 386 Test

## 🚀 Features
- Real-time object detection powered by fine-tuned **YOLO11**.
- Interactive Web GUI built with **Streamlit**.
- Dynamic confidence threshold adjustment.
- Instant object summary count per image.

## 📁 Repository Structure
helmet-detection-yolo11/
```text
.
├── app.py              # Main Streamlit web application
├── requirements.txt    # Python packages and dependencies
└── README.md           # Project documentation
