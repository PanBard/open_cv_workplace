import cv2 as cv
import numpy as np
import os
from time import time,sleep
from windowcapture import WindowCapture
from vision import Vision
from screenshot import Screenshot, KingReturn

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))



# capture1 = cv.VideoCapture(0)
capture = cv.VideoCapture("http://192.168.137.175:8080/video")

cascade_limestone = cv.CascadeClassifier('cascade.xml')

vision_limestone = Vision(None)
screenshot_found_probe = Screenshot()

loop_time = time()
while(True):
    _, frame = capture.read()
    # pp, frame1 = capture1.read()
    # cv.imshow("livestream", frame1)
    frame_for_process = frame.copy()



    # if capture.isOpened():
    #     width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
    #     height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    #
    #     print(width,height)

    rectangles = cascade_limestone.detectMultiScale(frame)

    # draw the detection results onto the original image
    detection_image = vision_limestone.draw_rectangles(frame, rectangles)




    #############################################
    if len(detection_image):
        screenshot_found_probe.make_screenshot(frame,frame_for_process,rectangles)

    # if screenshot_found_probe.freeze:
    #     while screenshot_found_probe.freeze:
    #         sleep(1)

    #############################################


    # display the images
    if KingReturn.FLAGA==False:
        cv.imshow('Matches', detection_image)
    elif KingReturn.FLAGA:
        cv.destroyAllWindows()
    #     print("dalsze instrukcje")
    #     cv.destroyWindow("Matches")


    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # elif key == ord('f'):
    #     cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    # elif key == ord('d'):
    #     cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')
