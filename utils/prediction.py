import tensorflow as tf
import numpy as np
from utils.image_processing import preprocess_image

# Load model chỉ một lần
model = tf.keras.models.load_model("models/VGG19_model.h5")

# Giả sử bạn có danh sách các class
class_names = ["Cat", "Dog", "Elephant"]  # Thay bằng danh sách của bạn

def predict_image(img_path):
    """Dự đoán class của ảnh."""
    processed_img = preprocess_image(img_path)
    predictions = model.predict(processed_img)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100  # Tỷ lệ %
    return predicted_class, confidence
