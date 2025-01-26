import cv2
import mediapipe as mp

# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start capturing from the webcam
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB before processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe hands
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:

            for hand_landmarks in result.multi_hand_landmarks:

                # Drawing hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmarks for finger counting
                landmarks = hand_landmarks.landmark

                # Define the tips of the fingers
                finger_tips = [landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y,
                               landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y,
                               landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y,
                               landmarks[mp_hands.HandLandmark.PINKY_TIP].y,
                               landmarks[mp_hands.HandLandmark.THUMB_TIP].x]
                
                # Get the landmarks of the corresponding lower knuckles for comparison
                knuckles = [landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP].y,
                            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y,
                            landmarks[mp_hands.HandLandmark.RING_FINGER_MCP].y,
                            landmarks[mp_hands.HandLandmark.PINKY_MCP].y,
                            landmarks[mp_hands.HandLandmark.THUMB_CMC].x]

                # Count fingers up (fingers are considered up if tip is above knuckle in the y-axis)
                fingers_up = [finger_tips[i] < knuckles[i] for i in range(4)]  # Four fingers except the thumb

                thumb_up = finger_tips[4] > knuckles[4]  # Thumb logic is reversed in horizontal axis

                # Combine thumb and other fingers to get full count
                if sum(fingers_up) == 4 and thumb_up:
                    print("five")

        # Show the frame with drawings
        cv2.imshow("Hand Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()