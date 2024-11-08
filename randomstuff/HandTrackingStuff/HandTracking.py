import cv2 as cv
import mediapipe as mp
import sys


def main():
    cap = cv.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    while True:
        succes, image = cap.read()
        imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = hands.process(imageRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 20:
                    cv.circle(image, (cx, cy), 25, (255, 0, 255), cv.FILLED)
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
        cv.imshow("Output ", image)
        cv.waitKey(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
