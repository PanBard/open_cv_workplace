import os
import pyautogui
from time import sleep, time
import pathlib
from class_only_for_variable import ForVariable

parent_directory = str(pathlib.Path(__file__).parent.resolve())+"\\"
directory = "cascade"

# create folder: cascade
path = os.path.join(parent_directory,directory)
if not os.path.exists(path):
    os.mkdir(path)



sample_variable = ForVariable()

positive_sample =20 #less than number of positive sample
negative_sample = 1000 #whatever
number_stages =13 #number of stages training
maxFalseAlarmRate = 0.4
minHitRate = 0.99
cascade_program_path = f"\\opencv\\build\\x64\\vc15\\bin\\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w {sample_variable.width} -h {sample_variable.height} -numPos {positive_sample} -numNeg {negative_sample} -numStages {number_stages} -maxFalseAlarmRate {maxFalseAlarmRate} -minHitRate {minHitRate}"

pyautogui.press('win')
sleep(0.5)
pyautogui.write('cmd')
pyautogui.press('enter')
sleep(1)

path = str(pathlib.Path(__file__).parent.resolve())
pyautogui.write(f"cd {path}")
pyautogui.press('enter')
pyautogui.write(path+cascade_program_path)
# pyautogui.press('enter')
