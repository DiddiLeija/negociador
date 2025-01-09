"""
Config de la ventana para administradores del negocio,
con funciones para alterar directamente el banco de
datos, credenciales, etc
"""

import tkinter
from .windowBase import Base
from .database import get_password_data


class AdminEditor(Base):
    def main_setup(self):
        pass  # TODO: fixme
