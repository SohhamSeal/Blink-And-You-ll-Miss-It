from keras_ocr import KerasOCR

# Load pre-trained Keras OCR model
ocr_model = KerasOCR()

# Define function to recognize speed limit
def recognize_speed_limit(image):
    text = ocr_model.recognize(image)
    speed_limits = {'20', '30', '50', '60', '70', '80', '90', '100', '110'}
    closest_match = min(speed_limits, key=lambda x:abs(len(x) - len(text)))
    return closest_match