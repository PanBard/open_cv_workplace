import cv2 as cv
import numpy as np
from threading import Thread, Lock

class Pomocnik:

    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None
    rectangles = []


    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        self.lock = Lock()
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method
        print("Inicjalizacja robotnika")

    def find(self, haystack_img, threshold=0.5, debug_mode=None):
        # run the OpenCV algorithm
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)
        print("find")
        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            print("pomocnik")
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)
        self.rectangles = rectangles
        print("koniec find pomocnika")

class Detektor:
    # threading properties
    stopped = True
    lock = None
    rectangles = []
    # properties
    cascade = None
    screenshot = None
    zrodlo_zdjecia = None
    poziom_precyzji = None

    def __init__(self, zrodelko, poziom):
        # create a thread lock object
        self.lock = Lock()
        self.zrodlo_zdjecia = zrodelko
        self.poziom_precyzji = poziom
        # load the trained model

    def zmiana(self, zdjecie, precyzja):
        self.lock.acquire()
        self.zrodlo_zdjecia = zdjecie
        self.poziom_precyzji = precyzja
        self.lock.release()

    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        print("powinie sie wylaczyc")
        self.stopped = True
        print("ale czy na pewno")

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            if not self.screenshot is None:
                # do object detection
                rectangles = self.rectangles
                pomoc = Pomocnik(self.zrodlo_zdjecia)
                points = pomoc.find(self.screenshot, self.poziom_precyzji, 'rectangles')
                # lock the thread while updating the results
                self.lock.acquire()
                self.rectangles = pomoc.rectangles
                self.lock.release()



class Vision:

    # given a list of [x, y, w, h] rectangles returned by find(), convert those into a list of
    # [x, y] positions in the center of those rectangles where we can click on those found items
    def get_click_points(self, rectangles):
        points = []

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))

        return points

    # given a list of [x, y, w, h] rectangles and a canvas image to draw on, return an image with
    # all of those rectangles drawn
    def draw_rectangles(self, haystack_img, rectangles):
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, lineType=line_type)
            print("Narysowano")
        return haystack_img

    # given a list of [x, y] positions and a canvas image to draw on, return an image with all
    # of those click points drawn on as crosshairs
    def draw_crosshairs(self, haystack_img, points):
        # these colors are actually BGR
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (center_x, center_y) in points:
            # draw the center point
            cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        return haystack_img

    def centeroid(self, point_list):
        point_list = np.asarray(point_list, dtype=np.int32)
        length = point_list.shape[0]
        sum_x = np.sum(point_list[:, 0])
        sum_y = np.sum(point_list[:, 1])
        return [np.floor_divide(sum_x, length), np.floor_divide(sum_y, length)]



def main():
    capture = cv.VideoCapture("http://192.168.137.175:8080/video")
    wykrywanie_obiektu = Detektor('probka.jpg', 0.8)
    vision = Vision()
    wykrywanie_obiektu.start()


    while (True):
        _, frame = capture.read()
        # cv.imshow("livestream", frame)

        wykrywanie_obiektu.update(frame)
        detection_image = vision.draw_rectangles(frame, wykrywanie_obiektu.rectangles)
        cv.imshow('Matches', detection_image)

        key = cv.waitKey(1)
        if key == ord('q'):
            wykrywanie_obiektu.stop()
            cv.destroyAllWindows()
            del wykrywanie_obiektu
            del vision
            print("niby koniec")
            break



main()
