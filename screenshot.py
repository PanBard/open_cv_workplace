import  cv2 as cv
from time import time
import os
import pathlib
from process_image import Process,ReturnFlag

class KingReturn:
    FLAGA = ReturnFlag.FLAGA


class Screenshot:
    licznik = 0
    directory_for_display = "screenshots"
    directory_for_process = "screenshots\\process"
    name_file = "1.txt"

    parent_directory = str(pathlib.Path(__file__).parent.resolve()) + "\\"
    path_for_display = os.path.join(parent_directory, directory_for_display)
    print("path_for_display: ",path_for_display)
    path_for_process = os.path.join(parent_directory, directory_for_process)
    print("path_for_process: ", path_for_process)
    p = Process(path_for_display=path_for_display,path_for_process=path_for_process)
    first_time = time()
    nr_zdjecia = 1
    freeze = False
    def make_screenshot(self,frame_for_display,frame_for_process,rect):
        if not os.path.exists( self.path_for_process):
            os.mkdir( self.path_for_process)
        if not os.path.exists( self.path_for_display):
            os.mkdir( self.path_for_display)
        loop_time = time()

        if loop_time - self.first_time >=5:
            cv.imwrite(f"{self.directory_for_display}/{self.nr_zdjecia}.jpg", frame_for_display)
            cv.imwrite(f"{self.directory_for_process}/{self.nr_zdjecia}.jpg", frame_for_process)
            self.first_time = time()
            self.nr_zdjecia +=1
            self.p.show_image(rect)
            self.freeze=True

