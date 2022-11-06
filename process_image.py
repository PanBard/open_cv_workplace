import  cv2
from time import time
import os.path
from sklearn.cluster import KMeans
import numpy as np
from time import sleep
from colour_classify import ColorClassify


class ReturnFlag:
    FLAGA = False

class Process:

    def __init__(self,path_for_display, path_for_process ):
        self.path_for_display = path_for_display
        self.path_for_process = path_for_process

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    def return_flaga(self):
        return True

    def czekaj(self,sekundy):
        sleep(sekundy)

    def show_image(self,rect):
        for (x, y, w, h) in rect:
            self.x1 = x  #
            self.y1 = y
            self.x2 = x + w
            self.y2 = y + h * 6

        self.y1= int((self.y2 - self.y1)/1.5) + self.y1

        folder = "./screenshots/"
        name_file = "/1.jpg"
        path_for_display= self.path_for_display + name_file
        path_for_process = self.path_for_process + name_file
        print(path_for_display)

        if os.path.isfile(path_for_display):

            ReturnFlag.FLAGA = True
            img_for_display = cv2.imread(path_for_display)
            img_for_process = cv2.imread(path_for_process)
            cv2.namedWindow("okno", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("okno", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            e = cv2.imshow("okno",img_for_display)


            # self.czekaj(8)
            # cv2.destroyWindow("okno")
            cropped_image = img_for_display[self.y1:self.y2,self.x1:self.x2 ]
            cropped_image_2 = img_for_process[self.y1:self.y2,self.x1:self.x2 ]

            cv2.imshow("przyciete",cropped_image)

            kop = ColorClassify()
            kop.show_component_color(cropped_image_2)







            k = cv2.waitKey(0)
        if k == ord("q"):
            cv2.destroyWindow("okno")
            print(rect)

    def visualize_Dominant_colors(cluster, C_centroids):
        C_labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        (C_hist, _) = np.histogram(cluster.labels_, bins=C_labels)
        C_hist = C_hist.astype("float")
        C_hist /= C_hist.sum()

        rect_color = np.zeros((50, 300, 3), dtype=np.uint8)
        img_colors = sorted([(percent, color) for (percent, color) in zip(C_hist, C_centroids)])
        start = 0
        for (percent, color) in img_colors:
            print(color, "{:0.2f}%".format(percent * 100))
            end = start + (percent * 300)
            cv2.rectangle(rect_color, (int(start), 0), (int(end), 50), \
                          color.astype("uint8").tolist(), -1)
            start = end
        return rect_color