import pyautogui
from time import sleep, time
import pathlib

class ForVariable:
    number_of_sample = 100  # bez znaczenia, ale musi byc wiekszy niz liczba zdjec
    width = 70  # in pixels
    height = 400  # in pixels



class Sample:

    def run(self):
        annotations_program_path = f"\\opencv\\build\\x64\\vc15\\bin\\opencv_createsamples.exe -info pos.txt -w {ForVariable.width} -h {ForVariable.height} -num {ForVariable.number_of_sample} -vec pos.vec"

        pyautogui.press('win')
        sleep(0.5)
        pyautogui.write('cmd')
        pyautogui.press('enter')
        sleep(1)

        path = str(pathlib.Path(__file__).parent.resolve())
        pyautogui.write(f"cd {path}")
        pyautogui.press('enter')
        pyautogui.write(path+annotations_program_path)
        # pyautogui.press('enter')



# def main():
#     sample = Sample()
#     sample.run()
#
# main()