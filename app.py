import streamlit as st
import os
from utils.prediction import predict_image

# Tiêu đề trang
st.title("🖼️ Ứng dụng Phân loại Ảnh với TensorFlow")

# Upload ảnh
uploaded_file = st.file_uploader("Chọn một ảnh để dự đoán", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Lưu ảnh vào thư mục uploads/
    img_path = os.path.join("uploads", uploaded_file.name)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Hiển thị ảnh
    st.image(img_path, caption="Ảnh đã tải lên", use_column_width=True)

    # Dự đoán ảnh
    predicted_class, confidence = predict_image(img_path)

    # Hiển thị kết quả
    st.write(f"**Dự đoán:** {predicted_class}")
    st.write(f"**Độ tin cậy:** {confidence:.2f}%")
