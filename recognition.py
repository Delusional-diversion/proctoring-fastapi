import face_recognition
from utils import base64_to_image

def verifyFaces(str1,str2):
    image1 = base64_to_image(str1)
    image2 = base64_to_image(str2)

    encoding1 = face_recognition.face_encodings(image1)
    encoding2 = face_recognition.face_encodings(image2)
    results = face_recognition.compare_faces([encoding1[0]], encoding2[0])
    return results[0]



# verifyFaces(base64_image_string,base64_image_string)


