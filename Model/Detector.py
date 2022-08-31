import cv2

def test(cv2image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
    gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y , w ,h) in faces:

        # Set boundary box for faces
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = cv2image[y:y+h, x:x+w]

        # Detect Eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 11)
        for (ex, ey ,ew, eh) in eyes:
            # Set boundary box for eyes
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)
    

    return cv2image

    