import os
import pyautogui
from time import sleep, time
import pathlib
from class_only_for_variable import ForVariable
from save_clean_old_cascade import Cleaner


class Training:

    def run(self):
        parent_directory = str(pathlib.Path(__file__).parent.resolve())+"\\"
        directory = "cascade"

        # create folder: cascade
        path = os.path.join(parent_directory,directory)
        if not os.path.exists(path):
            os.mkdir(path)



        sample_variable = ForVariable()
        clean_it = Cleaner()
        clean_it.run()

        cascade_program_path = f"\\opencv\\build\\x64\\vc15\\bin\\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w {sample_variable.width} -h {sample_variable.height} -numPos {sample_variable.positive_sample} -numNeg {sample_variable.negative_sample} -numStages {sample_variable.number_stages} -maxFalseAlarmRate {sample_variable.maxFalseAlarmRate} -minHitRate {sample_variable.minHitRate}"

        pyautogui.press('win')
        sleep(0.5)
        pyautogui.write('cmd')
        pyautogui.press('enter')
        sleep(1)

        path = str(pathlib.Path(__file__).parent.resolve())
        pyautogui.write(f"cd {path}")
        pyautogui.press('enter')
        pyautogui.write(path+cascade_program_path)
        print("4 Model is ready to run.")
        # pyautogui.press('enter')
