import numpy as np
from tensorflow.keras.preprocessing import image

def preprocess_image(img_path, target_size=(224, 224)):
    """Tiền xử lý ảnh trước khi đưa vào model."""
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Thêm batch dimension
    img_array /= 255.0  # Chuẩn hóa về [0,1]
    return img_array
