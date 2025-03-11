import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, min_detection_confidence=0.6, min_tracking_confidence=0.6):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
            max_num_hands=1
        )
    
    def find_hands(self, frame, draw=True):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False
        results = self.hands.process(rgb_frame)
        rgb_frame.flags.writeable = True
        
        if results.multi_hand_landmarks and draw:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        
        return frame, results
    
    def find_position(self, results, img_shape):
        h, w, _ = img_shape
        landmarks = []
        
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]  # First hand only
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append({'id': id, 'x': lm.x, 'y': lm.y, 'cx': cx, 'cy': cy})
        
        return landmarks
