import cv2
import dlib

from utils import base64_to_image

def detect_face_and_landmarks(image, shape_predictor_path):
    # Load the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the shape predictor model
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(shape_predictor_path)

    # Detect faces in the image
    faces = detector(gray)

    if not faces:
        return None, None, None  # Return None for face, landmarks, and faces

    # Assume only one face in the image for simplicity
    face = faces[0]

    # Predict facial landmarks
    landmarks = predictor(gray, face)

    return face, landmarks, faces

def analyze_face_movements(landmarks):
    # Assuming some basic rules for movement analysis
    # Replace these assumptions with a more sophisticated analysis based on your requirements

    # Example: Checking if the head is up
    head_up = landmarks.part(27).y < landmarks.part(30).y

    # Example: Checking if the head is turned right
    head_right = landmarks.part(2).x < landmarks.part(14).x

    # Example: Checking for blinking based on eye landmarks
    blinking = (
        landmarks.part(47).y < landmarks.part(46).y and
        landmarks.part(43).y < landmarks.part(44).y
    )

    return head_up, head_right, blinking

def proctoring_model(image_path, shape_predictor_path):
    face, landmarks, faces = detect_face_and_landmarks(image_path, shape_predictor_path)

    if face is None or landmarks is None or faces is None:
        return {'person_status': 'Face not detected', 'num_faces': 0}

    # Analyze facial movements
    head_up, head_right, blinking = analyze_face_movements(landmarks)

    # Example: Assuming a normal person status
    person_status = 'Normal'

    # Output dictionary
    output = {
        'person_status': person_status,
        'user_move1': 'Head up' if head_up else 'Head down',
        'user_move2': 'Head right' if head_right else 'Head left',
        'eye_movements': 'Blinking' if blinking else 'Not blinking',
        'num_faces': len(faces)
    }

    return output

# Example usage

shape_predictor_path = 'shape_predictor_68_face_landmarks.dat'
def proctor(str1):
    image = base64_to_image(str1)
    result = proctoring_model(image, shape_predictor_path)
    # print(result)
    return result


# proctor(base64_image_string)

