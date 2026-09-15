import os
import gdown
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Helmet & Safety Gear Detection",
    page_icon="⛑️",
    layout="centered"
)

st.title("⛑️ Helmet & Safety Gear Detection")
st.write("Upload an image to detect safety helmets and unprotected heads using **YOLO11**.")

# Download model from Google Drive if not present
file_id = "1LmHN095UzxVmUi435kQ65tEaRluirxVE"
url = f"https://drive.google.com/uc?id={file_id}"
output_path = "best.pt"

if not os.path.exists(output_path):
    with st.spinner("Downloading model... Please wait..."):
        gdown.download(url, output_path, quiet=False)

# Load model with caching
@st.cache_resource
def load_model():
    return YOLO(output_path)

try:
    model = load_model()
    st.sidebar.success("Model loaded successfully!")
except Exception as e:
    st.sidebar.error("Error loading model from Drive.")

# Sidebar controls
st.sidebar.header("Model Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.25, 0.05)

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)
        
    if st.button("Detect Safety Gear 🚀"):
        with st.spinner("Processing image..."):
            img_array = np.array(image.convert("RGB"))
            results = model.predict(source=img_array, conf=conf_threshold)
            
            res_plotted = results[0].plot()
            res_image = Image.fromarray(res_plotted)
            
            with col2:
                st.subheader("Detection Result")
                st.image(res_image, use_container_width=True)
                
            st.markdown("---")
            st.subheader("📊 Detection Summary:")
            boxes = results[0].boxes
            if len(boxes) > 0:
                class_names = model.names
                counts = {}
                for box in boxes:
                    cls_id = int(box.cls[0])
                    name = class_names[cls_id]
                    counts[name] = counts.get(name, 0) + 1
                
                for obj_name, count in counts.items():
                    st.write(f"- **{obj_name}**: {count}")
            else:
                st.write("No objects detected above the selected confidence threshold.")
