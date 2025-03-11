import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Disable pyautogui's failsafe
pyautogui.FAILSAFE = False

# Set up hand detection
with mp_hands.Hands(
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6,
    max_num_hands=1
) as hands:
    
    # Action cooldown to prevent rapid repeated actions
    last_action_time = 0
    cooldown = 0.2  # Reduced cooldown for better responsiveness
    
    # Status text
    current_action = "Ready"
    
    # Scroll settings
    scroll_amount = 50  # Pixels to scroll at once
    
    # Click settings
    last_click_time = 0
    click_cooldown = 0.5  # Seconds between clicks
    
    # Screen dimensions
    screen_width, screen_height = pyautogui.size()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR to RGB (keep flip for mirror-like experience)
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Improve processing performance
        rgb_frame.flags.writeable = False
        results = hands.process(rgb_frame)
        rgb_frame.flags.writeable = True

        # Get frame dimensions for scaling
        h, w, _ = frame.shape

        # Draw horizontal threshold lines for scroll zones
        scroll_up_line = int(0.3 * h)
        scroll_down_line = int(0.7 * h)
        
        cv2.line(frame, (0, scroll_up_line), (w, scroll_up_line), (0, 255, 0), 2)
        cv2.putText(frame, "SCROLL UP ZONE", (10, scroll_up_line - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
        cv2.line(frame, (0, scroll_down_line), (w, scroll_down_line), (0, 0, 255), 2)
        cv2.putText(frame, "SCROLL DOWN ZONE", (10, scroll_down_line - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get index finger tip (8) for primary control
                index_tip = hand_landmarks.landmark[8]
                
                # Get thumb tip for gesture detection
                thumb_tip = hand_landmarks.landmark[4]
                
                # Get middle finger tip and base for click detection
                middle_tip = hand_landmarks.landmark[12]
                index_base = hand_landmarks.landmark[5]
                
                # Extract positions
                index_x, index_y = index_tip.x, index_tip.y
                thumb_x, thumb_y = thumb_tip.x, thumb_tip.y
                
                # Convert to pixel coordinates for visualization
                px, py = int(index_x * w), int(index_y * h)
                
                # Draw a circle at index finger tip for better visualization
                cv2.circle(frame, (px, py), 15, (0, 255, 0), -1)
                
                # Draw hand landmarks for visual feedback
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Calculate distance between thumb and index finger for pinch detection
                thumb_index_distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                
                current_time = time.time()
                
                # MOUSE MOVEMENT - Direct mapping with increased speed
                # Map hand coordinates to screen with wider range - no duration for instant movement
                mouse_x = min(max(int((index_x * 1.5 - 0.25) * screen_width), 0), screen_width - 1)
                mouse_y = min(max(int((index_y * 1.5 - 0.25) * screen_height), 0), screen_height - 1)
                pyautogui.moveTo(mouse_x, mouse_y, duration=0.0)  # Immediate movement
                
                if current_time - last_action_time > cooldown:
                    # SCROLL UP - Hand in the upper zone
                    if index_y < 0.3:  # Above the upper line
                        current_action = "Scrolling Up"
                        pyautogui.scroll(scroll_amount)  # Positive for scrolling up
                        last_action_time = current_time
                    
                    # SCROLL DOWN - Hand in the lower zone
                    elif index_y > 0.7:  # Below the lower line
                        current_action = "Scrolling Down"
                        pyautogui.scroll(-scroll_amount)  # Negative for scrolling down
                        last_action_time = current_time
                
                # CLICK - Simplified click detection with pinch gesture
                if thumb_index_distance < 0.06:  # Tighter threshold for more precise detection
                    if current_time - last_click_time > click_cooldown:
                        current_action = "Clicked!"
                        pyautogui.click()  # Simple click at current position
                        last_click_time = current_time
                        # Visual feedback for click
                        cv2.circle(frame, (px, py), 30, (0, 0, 255), -1)
                else:
                    if current_action == "Clicked!":
                        current_action = "Ready"
                
                # Add hand position information
                cv2.putText(frame, f"Index X,Y: ({index_x:.2f}, {index_y:.2f})", (w - 250, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"Pinch: {thumb_index_distance:.3f}", (w - 250, 60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display status text prominently
        cv2.putText(frame, f"Action: {current_action}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Instructions for web interaction
        cv2.putText(frame, "WEB CONTROL: Hand ABOVE green line to SCROLL UP", (10, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "Hand BELOW red line to SCROLL DOWN", (10, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "PINCH thumb and index finger to CLICK", (10, 130), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Display the frame
        cv2.imshow("Web Page Gesture Control", frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
