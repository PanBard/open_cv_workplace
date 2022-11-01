import pyautogui
from time import sleep, time
import pathlib

annotations_program_path = "\\opencv\\build\\x64\\vc15\\bin\\opencv_annotation.exe --annotations=pos.txt --images=positive"
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
