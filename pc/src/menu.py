"Instrucciones para generar tanto la ventana de contraseña como el menu."

import tkinter
from .windowBase import Base
from .database import get_password_data


class Password(Base):
    # la ventana de la contraseña....

    def main_setup(self):
        self.pwd_data = get_password_data()
        self.password_capture = tkinter.StringVar()
        self.user_capture = tkinter.StringVar()
        if self.pwd_data is None:
            self.root.quit()
        # TODO: esto debe ser una imagen de logotipo [grande]
        tkinter.Label(
            self.frame, text="(Imagen aqui)"
        ).grid(column=0, row=0)
        # Label de instrucciones - usuario
        tkinter.Label(
            self.frame,
            text=u"Usuario:",
            bg="whitesmoke",
            fg="black",
            font=("Calibri", "14", "bold")
        ).grid(column=0, row=1)
        # Entrada de usuario
        # TODO: evaluar la posibilidad de un Menu de cascada
        # en lugar de una captura de texto, evitando errores
        # (pero, es lo mejor???)
        tkinter.Entry(
            self.frame,
            textvariable=self.user_capture,
            width=40,
            font=("Calibri", "14", "bold")
        ).grid(column=1, row=1)
        # Label de instrucciones - contraseña
        tkinter.Label(
            self.frame,
            text=u"Contraseña:",
            bg="whitesmoke",
            fg="black",
            font=("Calibri", "14", "bold")
        ).grid(column=0, row=2)
        # Entrada de contraseña
        tkinter.Entry(
            self.frame,
            textvariable=self.password_capture,
            show="*",
            width=40,
            font=("Calibri", "14", "bold")
        ).grid(column=1, row=2)
        # Botón de cierre
        tkinter.Button(
            self.frame,
            text="Cancelar y salir",
            command=self.root.quit,
            bg="red",
            fg="white",
            font=("Calibri", "14", "bold")
        ).grid(column=0, row=3)
        # Botón de acceso
        tkinter.Button(
            self.frame,
            text="Ingresar",
            command=self.enter_password,
            bg="green",
            fg="white",
            font=("Calibri", "14", "bold")
        ).grid(column=1, row=3)
    
    def enter_password(self):
        # TODO: fixme
        pass


class Menu(Base):
    def main_setup(self):
        pass  # TODO: fixme
