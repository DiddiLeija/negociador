"Manejo de la base de datos con SQLite."

import sqlite3
from . import tools

def open_database(name: str) -> tuple:
    "intenta abrir una base de datos y reporta el resultado."
    reason = ""
    try:
        con = sqlite3.connect(name)
    except Exception as exc:
        con = None
        reason = str(exc)
    if con is not None:
        try:
            cur = con.cursor()
        except Exception as exc:
            # NOTE: no conozco personalmente un caso en el que
            # sqlite3.cursor falle, pero cabe la posibilidad por
            # factores externos (cerrar el archivo, ctrl+c/z, etc) (?)
            cur = None
            reason = str(exc)
    if con is None or cur is None:
        tools.msg_err(
            f"No es posible {"abrir" if con is None else "manipular"} la base de datos '{name}' "
            f"a causa de un error interno no esperado ('{reason}').\n\n"
            f"Consulte al administrador del equipo o pida ayuda en {tools.links["issues"]}"
        )
    return con, cur  # si uno de los dos es None, la operacion superior debe cancelarse

def get_password_data():
    # localiza las contraseñas guardadas y presenta una.
    con, cur = open_database("data/user.sqlite")
    if con is None or cur is None:
        return None  # la operacion superior probablemente se deba cancelar (o todo el programa?)
    # ...
    # TODO: fixme
