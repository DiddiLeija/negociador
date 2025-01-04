"Herramientas usadas a lo largo del codigo."

import re

from tkinter import messagebox

def msg_info(msg, title=None):
    title = str(title)  # pq es imposible dar un default generico?
    messagebox.showinfo(title, msg)

def msg_warn(msg, title=None):
    title = "Advertencia!" if title is None else str(title)
    messagebox.showwarning(title, msg)

def msg_err(msg, title=None):
    title = "Error critico" if title is None else str(title)
    messagebox.showwerror(title, msg)

def is_strong_password(password):
    # Utilidad para evaluar la fuerza de una contraseña
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False
