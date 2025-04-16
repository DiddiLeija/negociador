"Negociador (PC)"

# TODO: sortear las importaciones con un formateador?

import tkinter
import PIL as pillow

from src import tools, menu, admin_editor

VERSION = (1, 0, 0, "dev1")


class Main:

    def __init__(self, name):
        self.root = tkinter.Tk(screenName=name)
        self.name = name
        self.root.title(
            f"{self.name} {VERSION[0]}.{VERSION[1]}.{VERSION[2]}{VERSION[3]}"
        )
        self.frames = list()
        self.build_frames()
        self.version = VERSION
        self.frames[0].build_frame()
        self.current_frame = self.frames[0]

    def build_frames(self):
        # truco para generar frames frescas. la meta de separar las frames en varios
        # archivos vuelve todo un poco mas dificil, pero no imposible...
        self.frames = [
            menu.Password(self.root),            # [0]
            menu.Menu(self.root),                # [1]
            admin_editor.AdminEditor(self.root)  # [2]
        ]
        # TODO: hay algun metodo mas apropiado?

    def switch_to(self, nxt):
        # funcion que podemos pasarle a las clases
        # de las frames para hacer un switch desde ahi.
        # NOTE: no es estable, hacer tests para confirmar comportamiento
        self.current_frame.frame.grid_remove()
        self.frames[nxt].build_frame()
        self.current_frame = self.frames[nxt]


if __name__ == "__main__":
    mainTk = Main("Negociador")
    mainTk.root.mainloop()
