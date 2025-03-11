import math
import cv2

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def draw_gesture_zones(frame, up_threshold=0.3, down_threshold=0.7):
    """Draw gesture zones on the frame."""
    h, w, _ = frame.shape
    
    # Scroll up zone
    scroll_up_line = int(up_threshold * h)
    cv2.line(frame, (0, scroll_up_line), (w, scroll_up_line), (0, 255, 0), 2)
    cv2.putText(frame, "SCROLL UP ZONE", (10, scroll_up_line - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Scroll down zone
    scroll_down_line = int(down_threshold * h)
    cv2.line(frame, (0, scroll_down_line), (w, scroll_down_line), (0, 0, 255), 2)
    cv2.putText(frame, "SCROLL DOWN ZONE", (10, scroll_down_line - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    return frame

def draw_instructions(frame):
    """Draw instruction text on the frame."""
    cv2.putText(frame, "WEB CONTROL: Hand ABOVE green line to SCROLL UP", (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "Hand BELOW red line to SCROLL DOWN", (10, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "PINCH thumb and index finger to CLICK", (10, 130), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    return frame

