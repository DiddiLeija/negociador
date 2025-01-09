"Instrucciones para generar tanto la ventana de contraseña como el menu."

import tkinter
from .windowBase import Base
from .database import get_password_data


class Password(Base):
    # la ventana de la contraseña....

    def main_setup(self):
        self.pwd_data = get_password_data()
        self.pwasword_capture = tkinter.StringVar()
        if self.pwd_data is None:
            self.root.quit()
        # TODO: esto debe ser una imagen de logotipo [grande]
        tkinter.Label(
            self.frame, text="(Imagen aqui)"
        ).grid(column=0, row=0)
        # Label de instrucciones
        tkinter.Label(
            self.frame,
            text=u"Introduzca su contraseña.",
            bg="whitesmoke",
            fg="black",
            font=("Calibri", "14", "bold")
        ).grid(column=1, row=0)
        # TODO: menu de cascada en (column=0, row=1) para elegir el usuario
        #       (requiere acceso a la lista de claves)
        # ...
        # Entrada de contraseña
        tkinter.Entry(
            self.frame,
            textvariable=self.pwasword_capture,
            show="*",
            width=40,
            font=("Calibri", "14", "bold")
        ).grid(column=1, row=1)
        # Botón de cierre
        tkinter.Button(
            self.frame,
            text="Cancelar y salir",
            command=self.root.quit,
            bg="red",
            fg="white",
            font=("Calibri", "14", "bold")
        ).grid(column=0, row=2)
        # Botón de acceso
        tkinter.Button(
            self.frame,
            text="Ingresar",
            command=self.enter_password,
            bg="green",
            fg="white",
            font=("Calibri", "14", "bold")
        ).grid(column=1, row=2)
    
    def enter_password(self):
        # TODO: fixme
        pass


class Menu(Base):
    def main_setup(self):
        pass  # TODO: fixme
