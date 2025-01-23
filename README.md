# Volume Controller Using Hand Gestures

This project utilizes computer vision and machine learning libraries to control the volume of a system through hand gestures. By tracking the position of specific landmarks on the user's hand using a webcam, the program adjusts the system's volume accordingly.  

---

## Features  
- **Gesture Detection**: Detects the forefinger and middle finger using **MediaPipe Hands**.  
- **Distance Measurement**: Calculates the distance between two landmarks (forefinger and middle finger) to determine the action.  
- **Volume Control**: Increases or decreases system volume based on the distance between the two fingers.  
- **Real-Time Processing**: The program operates in real-time with input from a webcam.

---

## How It Works  

1. **Webcam Input**:  
   The program starts by capturing real-time input from the webcam using the **OpenCV** library.  

2. **Hand Tracking**:  
   The **MediaPipe Hands** solution is used to detect and track the hand in the captured frames. It identifies the key landmarks on the hand and their corresponding coordinates.  

3. **Landmark Identification**:  
   Specific landmarks are identified:
   - Landmark 8: Tip of the forefinger.  
   - Landmark 12: Tip of the middle finger.  

4. **Distance Calculation**:  
   The Euclidean distance between the landmarks of the forefinger and middle finger is calculated using the formula:  
   ```
   distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) * 0.5 // 4
   ```

5. **Volume Adjustment**:  
   - If the distance exceeds a threshold (300), the system volume is increased.  
   - If the distance is less than the threshold, the system volume is decreased.  
   This is achieved using the **PyAutoGUI** library to send volume control commands to the system.

6. **Visualization**:  
   The program provides a visual representation of the tracked landmarks, highlights the key points, and draws a line between them in the live webcam feed.

---

## Libraries Used  
- **OpenCV**: For capturing real-time video feed and processing images.  
- **MediaPipe**: For detecting and tracking hand landmarks.  
- **PyAutoGUI**: For controlling the system volume programmatically.
