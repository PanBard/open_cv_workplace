import pyautogui
from time import sleep, time
import pathlib
from class_only_for_variable import ForVariable

forfun = ForVariable()

class Sample:

    def run(self):
        annotations_program_path = f"\\opencv\\build\\x64\\vc15\\bin\\opencv_createsamples.exe -info pos.txt -w {forfun.width} -h {forfun.height} -num {forfun.number_of_sample} -vec pos.vec"

        pyautogui.press('win')
        sleep(0.5)
        pyautogui.write('cmd')
        pyautogui.press('enter')
        sleep(1)

        path = str(pathlib.Path(__file__).parent.resolve())
        pyautogui.write(f"cd {path}")
        pyautogui.press('enter')
        pyautogui.write(path+annotations_program_path)
        pyautogui.press('enter')
        pyautogui.write('exit')
        pyautogui.press('enter')
        sleep(1)
        print("2 New sample was created")

    def delete_old_sample(self):
        pyautogui.press('win')
        sleep(0.5)
        pyautogui.write('cmd')
        pyautogui.press('enter')
        sleep(1)
        path = str(pathlib.Path(__file__).parent.resolve())
        pyautogui.write(f"cd {path}")
        pyautogui.press('enter')

        pyautogui.write('del pos.vec')
        pyautogui.press('enter')
        pyautogui.write('exit')
        pyautogui.press('enter')
        sleep(1)
        print("\n1 Old sample: 'pos.vec' was deleted")
# def main():
#     sample = Sample()
#     sample.delete_old_sample()
#     sample.run()
#
# main()