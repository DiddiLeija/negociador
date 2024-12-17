"Biblioteca para manejo de errores."

from tkinter import messagebox

def msg_info(msg, title=None):
    title = str(title)  # es imposible dar un default generico?
    messagebox.showinfo(title, msg)

def msg_warn(msg, title=None):
    title = "Advertencia!" if title is None else str(title)
    messagebox.showwarning(title, msg)

def msg_err(msg, title=None):
    title = "Error critico" if title is None else str(title)
    messagebox.showwerror(title, msg)
