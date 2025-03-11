#  Gesture Control for Web Browsing

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-yellow.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8+-orange.svg)

Control your web browser using only hand gestures! This computer vision project allows you to scroll, navigate, and click on web pages without touching your keyboard or mouse.

## Features

- ** Intuitive Cursor Control**: Control your mouse cursor by pointing with your index finger
- ** Smart Scrolling**: Scroll up or down by moving your hand to designated screen zones
- ** Natural Click Interaction**: Click by pinching your thumb and index finger together
- ** Real-time Visual Feedback**: On-screen indicators showing gesture recognition and actions

## Requirements

- Python 3.6+
- Webcam
- Dependencies:
  - OpenCV
  - MediaPipe
  - PyAutoGUI

##  Installation

1. Clone this repository:
2. Install required packages:
##  Usage

Run the main application:
### Control Guide

| Gesture | Action |
|---------|--------|
| Point with index finger | Move cursor |
| Move hand above green line | Scroll up |
| Move hand below red line | Scroll down |
| Pinch thumb and index finger | Click |
| Press 'q' on keyboard | Exit application |

##  Project Structure
### Control Guide

| Gesture | Action |
|---------|--------|
| Point with index finger | Move cursor |
| Move hand above green line | Scroll up |
| Move hand below red line | Scroll down |
| Pinch thumb and index finger | Click |
| Press 'q' on keyboard | Exit application |

##  Project Structure
## ⚙ How It Works

This project uses:
- **MediaPipe** for accurate hand landmark detection
- **OpenCV** for webcam access and visual interface
- **PyAutoGUI** to control mouse and keyboard actions

The application detects key points on your hand in real-time and translates specific gestures into computer inputs, allowing for touchless interaction with web content.

##  Customization

Adjust these variables in `gesture_control.py` to customize the experience:

- `scroll_amount`: Change scroll speed/distance
- `cooldown`: Adjust response sensitivity
- Scroll zone thresholds (currently at 30% and 70% of frame height)

##  Contributing

Contributions are welcome

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for their hand tracking solution
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for system control integration
