import face_recognition
import base64
from io import BytesIO
def base64_to_image(base64_string):
    # Decode the base64 string to binary data
    binary_data = base64.b64decode(base64_string)
    
    # Convert binary data to image
    image = face_recognition.load_image_file(BytesIO(binary_data))
    
    return image
