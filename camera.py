import cv2
from threading import Thread, Lock

class Camereon:
    window_name = "alibabskomarok"
    def __init__(self):
        self.lock = Lock()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        camera = cv2.VideoCapture(0)
        while not self.stopped:
            _, frame = camera.read()

            cv2.namedWindow("okp", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("okp", (300, 300))
            cv2.moveWindow("okp", 1000, 0)
            cv2.setWindowProperty("okp", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

            cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(self.window_name, (500, 300))
            cv2.moveWindow(self.window_name,500,0)
            cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

            cv2.imshow(self.window_name, frame)
            cv2.imshow("okp", frame)
            key = cv2.waitKey(1)

            if key == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()
