import cv2
import mediapipe as mp
import pyautogui

# Declare the variables in order to draw tye line between the fingers
x1_axis = y1_axis = x2_axis = y2_axis = 0
# In the webcam I store the result of the capture image by the webcam
webcam = cv2.VideoCapture(0)
# MAke the objects in order to capture the hand and draw points in it
my_hand = mp.solutions.hands.Hands()
drawing_points = mp.solutions.drawing_utils

# To show the capture image in the window I used the while loop
while True:
    _, image = webcam.read()
    image=cv2.flip(image,1)
    # now convert the capture image into the RGB (Red,Green,Blue) Format for the OpenCV library bcz it use that as default
    screen_height, screen_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # now capture all the hands in the webcam
    output = my_hand.process(rgb_image)
    hand_present = output.multi_hand_landmarks
    # checker whether any hand available or not
    if hand_present:
        for hand in hand_present:
            drawing_points.draw_landmarks(image, hand)
            hand_points = hand.landmark
            for id_no, hand_point in enumerate(hand_points):
                x_axis = int(hand_point.x * screen_width)
                y_axis = int(hand_point.y * screen_height)
                # the point of the fore-finger landmark id_no is 8 and for the middlefinger is 12
                if id_no == 12:
                    cv2.circle(img=image,center=(x_axis,y_axis),radius = 5 ,color=(255,255,255),thickness=3)
                    x1_axis=x_axis
                    y1_axis=y_axis
                if id_no == 8:
                    cv2.circle(img=image,center=(x_axis,y_axis),radius = 5 ,color=(0,255,0),thickness=3)
                    x2_axis=x_axis
                    y2_axis=y_axis

        # Formula to calculate the distance between the fingers
        distance = ((x2_axis - x1_axis) ** 2 + (y2_axis - y1_axis) ** 2) * 0.5 // 4
        cv2.line(image, pt1=(x1_axis,y1_axis),pt2=(x2_axis,y2_axis),color=(0,0,255),thickness=3)
        if distance > 300:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("Volume Controller using Hand Gestures", image)
    Pressed_key = cv2.waitKey(10)
    #  To close the webcam window whenever you press enter it will close the window
    # Ascii of enter 13.
    if Pressed_key == 13:
        break
webcam.release()
cv2.destroyAllWindows()