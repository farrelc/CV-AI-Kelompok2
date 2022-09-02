import cv2

def get_face_and_eye(cv2image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
    gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)

    face_detected = False
    eye_detected = False

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y , w ,h) in faces:

        # Set boundary box for faces
        cv2.rectangle(cv2image, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = cv2image[y:y+h, x:x+w]

        # face detected
        face_detected = True

        # Detect Eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 11)
        for (ex, ey ,ew, eh) in eyes:
            # Set boundary box for eyes
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)

            # eye detected
            eye_detected = True
    
    return cv2image, face_detected, eye_detected

    