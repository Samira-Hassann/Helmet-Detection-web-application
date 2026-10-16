# ⛑️ Helmet & Safety Gear Detection (YOLO11m)

An end-to-end Computer Vision project designed to automatically detect safety compliance in industrial environments by identifying whether workers are wearing safety helmets (`helmet`) or working with unprotected heads (`head`) using **YOLO11** and **Streamlit**.

🚀 **Live Demo:** [Helmet Detection Web App](https://helmet-detection-web-application.streamlit.app/)  
📌 **Kaggle Notebook:** [Helmet & Safety Gear Detection (YOLO11)](https://www.kaggle.com/code/samoura/helmet-safety-gear-detection-yolo11)

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

## 🚀 Model Training & Performance
* **Architecture:** YOLO11m (Ultralytics)
* **Training Setup:** Fine-tuned , layer freezing, and automated hyperparameter optimization using AdamW.
* **Test Metrics:**
  * **Precision (mP):** ~93.7%
  * **Recall (mR):** ~92.7%
  * **mAP@50:** ~96.5%
  * **mAP@50-95:** ~60.5%


## 📁 Repository Structure
helmet-detection-yolo11/
```text
.
├── app.py              # Main Streamlit web application
├── requirements.txt    # Python packages and dependencies
└── README.md           # Project documentation
```



