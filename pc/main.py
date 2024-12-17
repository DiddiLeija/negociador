"Negociador (PC)"

# TODO: sortear las importaciones con un formateador

import tkinter
import PIL as pillow

from src import errors, menu, admin_editor

VERSION = (1, 0, 0)

class Main:

    def __init__(self, name):
        self.root = tkinter.Tk(screenName=name)
        self.name = name
        self.version = VERSION

if __name__ == "__main__":
    mainTk = Main("Negociador")
    mainTk.root.mainloop()
