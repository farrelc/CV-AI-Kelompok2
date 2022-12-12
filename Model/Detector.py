import cv2 as cv
import mediapipe as mp
import math
import numpy as np
  

# landmark detection function 
def landmarksDetection(img, results):
    img_height, img_width= img.shape[:2]
    # list[(x,y), (x,y)....]
    mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in results.multi_face_landmarks[0].landmark]

    # returning the list of tuples for each landmarks 
    return mesh_coord

# Euclaidean distance 
def euclaideanDistance(point, point1):
    x, y = point
    x1, y1 = point1
    distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    return distance

# Blinking Ratio
def closingEyeRatio(landmarks, right_indices, left_indices):
    # Right eyes 
    # horizontal line 
    rh_right = landmarks[right_indices[0]]
    rh_left = landmarks[right_indices[8]]
    # vertical line 
    rv_top = landmarks[right_indices[12]]
    rv_bottom = landmarks[right_indices[4]]

    # LEFT_EYE 
    # horizontal line 
    lh_right = landmarks[left_indices[0]]
    lh_left = landmarks[left_indices[8]]

    # vertical line 
    lv_top = landmarks[left_indices[12]]
    lv_bottom = landmarks[left_indices[4]]

    rhDistance = euclaideanDistance(rh_right, rh_left)
    rvDistance = euclaideanDistance(rv_top, rv_bottom) + 1e-8

    lvDistance = euclaideanDistance(lv_top, lv_bottom) + 1e-8
    lhDistance = euclaideanDistance(lh_right, lh_left)

    reRatio = rhDistance/rvDistance
    leRatio = lhDistance/lvDistance

    ratio = (reRatio+leRatio) / 2
    return ratio 


def get_face_and_eye(cv2image):

    # face mesh model
    map_face_mesh = mp.solutions.face_mesh

    # Stats
    eyes_closed = False
    face_detected = False

    # Left eyes indices 
    LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398]

    # right eyes indices
    RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246]

    # Face
    FACE = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103,67, 109]

    # Run face mesh Model
    with map_face_mesh.FaceMesh(min_detection_confidence = 0.7, min_tracking_confidence=0.1) as face_mesh:

        #  resizing frame
        frame = cv.resize(cv2image, None, fx=1, fy=1, interpolation=cv.INTER_CUBIC)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

        # Face Mesh Detection
        results  = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            
            # Update face detection stats
            face_detected = True

            # Get face mesh Coordinates
            mesh_coords = landmarksDetection(frame, results)

            # Draw face and eyes in frame
            cv.polylines(frame, [np.array([mesh_coords[p] for p in LEFT_EYE], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
            cv.polylines(frame, [np.array([mesh_coords[p] for p in RIGHT_EYE], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
            cv.polylines(frame, [np.array([mesh_coords[p] for p in FACE], dtype=np.int32)], True, (0,255,0), 1, cv.LINE_AA)
                        
            # Closing Eye Ratio
            ratio = closingEyeRatio(mesh_coords, RIGHT_EYE, LEFT_EYE)

            # Eye closed stats update
            eyes_closed = True if ratio > 3.75 else False
  
    return frame, face_detected, eyes_closed
