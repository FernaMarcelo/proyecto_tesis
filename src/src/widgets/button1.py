# Importaciones
import flet as ft
import asyncio


class ButtonScreen(ft.UserControl):
    def __init__(self, route_change_handler, nav_rail_class, page):
        super().__init__()
        self.route_change_handler = route_change_handler
        self.nav_rail_class = nav_rail_class
        self.page = page

    def build(self):
        rail = self.nav_rail_class.create_rail()
        peo = ft.ElevatedButton("Disabled button", disabled=True)
        # Agregar el paréntesis de cierre correcto después de la lista de controles
        return ft.Row(controls=[rail, peo])
