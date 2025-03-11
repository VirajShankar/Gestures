import cv2
from hand_detector import HandDetector

def main():
    # Initialize detector
    detector = HandDetector()
    
    # Start webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read frame
        success, img = cap.read()
        if not success:
            break
            
        # Find hands
        img = cv2.flip(img, 1)  # Mirror effect
        img, results = detector.find_hands(img)
        
        # Get position
        if results.multi_hand_landmarks:
            landmarks = detector.find_position(results, img.shape)
            
            # Display landmark count if detected
            if landmarks:
                cv2.putText(img, f"Landmarks: {len(landmarks)}", (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display
        cv2.imshow("Test", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

