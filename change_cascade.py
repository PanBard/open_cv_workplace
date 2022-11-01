import pyautogui
from time import sleep, time
import pathlib

pyautogui.press('win')
sleep(0.5)
pyautogui.write('cmd')
pyautogui.press('enter')
sleep(1)
path = str(pathlib.Path(__file__).parent.resolve())
pyautogui.write(f"cd {path}")
pyautogui.press('enter')

pyautogui.write('del cascade.xml')
pyautogui.press('enter')
pyautogui.write('cd cascade')
pyautogui.press('enter')
pyautogui.write(f'copy cascade.xml {path}')
pyautogui.press('enter')
print(path)
