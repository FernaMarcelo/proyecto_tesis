import flet as ft
from flet import UserControl

class PrincipalScreen(UserControl):

    def __init__(self, page):
        self.page = page

    def build(self):
        # Contenedor principal para los gráficos
        container = ft.Column()

        # Aquí podrías añadir tus gráficos y botones a `container.controls`
        # ...

        return container
