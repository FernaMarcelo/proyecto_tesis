import flet as ft
from flet import Page, Row, ElevatedButton, TextField, Text, UserControl
from flet.plotly_chart import PlotlyChart
from widgets.nav import NavigationRailClass

from ui.grafico_line import GraphScreen

def main(page: ft.Page):

    page.title = "Routes Example"

    def handle_route_change(route):
        page.go_async(route)

    destinations = [
        {"route": "/inicio", "icon": ft.icons.STACKED_BAR_CHART, "label": "marcelito"},
        {"route": "/graficos", "icon": ft.icons.STACKED_BAR_CHART, "label": "felipoto"},
    ]

    nav_rail = NavigationRailClass(handle_route_change, destinations, page)



    def route_change(e):
        if page.route == "/graficos":
            chanchito = GraphScreen(handle_route_change,nav_rail)
            page.views.append(ft.View("/graficos", controls=[chanchito], bgcolor="#1f262f"))

        page.update()


    page.on_route_change = route_change
    page.go("/graficos")

ft.app(target=main, view=ft.AppView.FLET_APP)
