import  cv2 as cv
from time import time
import os
import pathlib


# capture = cv.VideoCapture(0, cv.CAP_DSHOW)
# capture.set(cv.CAP_PROP_FRAME_WIDTH,640)
# capture.set(cv.CAP_PROP_FRAME_HEIGHT,480)

licznik = 0
directory = "camera_images"

parent_directory = str(pathlib.Path(__file__).parent.resolve())+"\\"

# create folder: old_cascades
path = os.path.join(parent_directory,directory)
if not os.path.exists(path):
    os.mkdir(path)







capture = cv.VideoCapture("http://192.168.137.175:8080/video")
# capture = cv.VideoCapture(0)




while(True):
    _, frame = capture.read()
    cv.imshow("livestream", frame)

    key = cv.waitKey(1)

    # if capture.isOpened():
    #     width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
    #     height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    #
    #     print(width,height)

    loop_time = time()

    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('s'):
        cv.imwrite(f"{directory}/{loop_time}.jpg", frame)
        print(f"cyk {licznik}")
        licznik +=1