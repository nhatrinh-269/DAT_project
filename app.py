import streamlit as st
import os
from utils.prediction import predict_image

# Page title
st.title("🖼️ Image Classification App with TensorFlow")

# Upload image
uploaded_file = st.file_uploader("Choose an image for prediction", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Save image to uploads/ directory
    img_path = os.path.join("uploads", uploaded_file.name)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display uploaded image
    st.image(img_path, caption="Uploaded Image", use_column_width=True)

    # Predict image
    predicted_class, confidence = predict_image(img_path)

    # Display result
    st.write(f"**Prediction:** {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}%")