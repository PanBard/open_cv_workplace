import os
import pathlib
import pyautogui
from time import time, sleep

class Cleaner:
    def run(self):
        directory = "old_cascades"

        parent_directory = str(pathlib.Path(__file__).parent.resolve())+"\\"

        # create folder: old_cascades
        path = os.path.join(parent_directory,directory)
        if not os.path.exists(path):
            os.mkdir(path)
            path1 = path + "\\no.txt"
            with open(path1,'w') as file:
                file.write("0")
            print("Made brand new file")

        path2 = path + "\\no.txt"
        with open(path2,'r+') as file:
            text = file.readline()
            file.seek(0)
            number = int(text)
            saved_number = str(number+1)
            file.write(saved_number)

        if number!=0:
            pyautogui.press('win')
            sleep(0.5)
            pyautogui.write('cmd')
            pyautogui.press('enter')
            sleep(1)
            pyautogui.write("cd "+parent_directory.rstrip("\\"))
            sleep(0.1)
            pyautogui.press('enter')
            pyautogui.write(f'copy cascade.xml {path}')
            pyautogui.press('enter')
            pyautogui.write("cd " + path)
            pyautogui.press('enter')
            pyautogui.write(f"ren cascade.xml {number}.xml")
            pyautogui.press('enter')
            pyautogui.write("cd " + parent_directory+"cascade")
            pyautogui.press('enter')
            pyautogui.write("del * /S /Q")
            pyautogui.press('enter')
            pyautogui.write('exit')
            pyautogui.press('enter')
            sleep(1)
            print("3 Old cascade was successfully coped and dir is empty ")

