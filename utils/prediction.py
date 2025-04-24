import tensorflow as tf
import numpy as np
from utils.image_processing import preprocess_image

# Load the model only once
model = tf.keras.models.load_model("models/VGG19_model.h5")

# Assume you have a list of class names
class_names = ["Early Pre-B", "Pre-B", "Pro-B", "Benign"]  # Replace with your actual class names

def predict_image(img_path):
    """Predict the class of an image."""
    processed_img = preprocess_image(img_path)
    predictions = model.predict(processed_img)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100  # Convert to percentage
    return predicted_class, confidence
