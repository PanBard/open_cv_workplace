import cv2
import mediapipe as mp
import time

class HandTracker():

    def __init__(self,static_image_mode = False,max_num_hands = 2,model_complexity = 1, min_detection_confidence = 0.5,min_tracking_confidence = 0.5):
        self.static_image_mode =static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    def trackHand(self,img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img





def main():
    cap = cv2.VideoCapture(0)
    pTime = 0

    tracker = HandTracker()
    while True:
        success, img = cap.read()
        img = tracker.trackHand(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN,
        #             3, (0, 255, 0), 3)
        cv2.imshow("kamerkoni", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()