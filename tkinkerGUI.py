import tkinter as tk
from camera import Camereon


class MyGUI:
    kapejszyn = Camereon()
    def __init__(self):
        self.root = tk.Tk()
        self.w = 500  # width for the Tk root
        self.h = 300  # height for the Tk root

        self.ws = self.root.winfo_screenwidth()  # width of the screen
        self.hs = self.root.winfo_screenheight()  # height of the screen
        print(self.hs,self.ws)
        # calculate x and y coordinates for the Tk root window
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, 0, 0))
        
        self.root.title("My First number")

        self.label = tk.Label(self.root, text="Jol men",font=('Verdana',18))
        self.label.pack(padx=20,pady=20)

        self.button = tk.Button(self.root, text="Uruchamianie kamery", font=('Verdana',18), command=self.show_camera)
        self.button.pack()

        self.button = tk.Button(self.root, text="Wylaczanie kamery", font=('Verdana', 18), command=self.stop_camera)
        self.button.pack()

        self.root.mainloop()
    def show_camera(self):

        self.kapejszyn.start()

    def stop_camera(self):
        self.kapejszyn.stop()


def main():
    gui = MyGUI()



main()