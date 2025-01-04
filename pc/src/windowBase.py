"Base de las ventanas."

import tkinter
from abc import ABC, abstractmethod


class Base(ABC):
    """
    Clase guia de todas las ventanas de la app.
    Todos los objetos de ventana heredan de alguna manera
    a esta clase inicial.
    """
    invoke_next = ""
    finished = False
    frame = None

    def __init__(self, root):
        self.root = root
        self.grid = True  # TODO: opcional

    @abstractmethod
    def main_setup(self):
        # La principal magia de las clases herederas, que las configura
        # de acuerdo a su funcion. Todas las herederas deben alterar
        # su propio main_setup() o arrojan un error, al ser el original un
        # metodo abstracto.
        pass

    def build_frame(self):
        # Secuencia interna de arranque.
        self.frame = tkinter.Frame(self.root)
        if self.grid:
            self.frame.grid()
        self.main_setup()  # asumiendo que ya no es un metodo abstracto en la instancia
