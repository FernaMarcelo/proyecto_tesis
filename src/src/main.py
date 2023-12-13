import flet as ft
from flet import Page, Row, ElevatedButton, TextField, Text, UserControl
from flet.plotly_chart import PlotlyChart
from widgets.nav import NavigationRailClass
from ui.button1 import ButtonScreen
from ui.grafico_line import obtener_datos_para_grafico, crear_figura_plotly

def main(page: ft.Page):
    page.title = "Routes Example"

    def handle_route_change(route):
        if route == "/inicio":
            page.update()  # Actualiza la página para mostrar la nueva vista
        elif route == "/graficos":
            grafico_screen = grafico_desempeno_view()
            page.update()  # Actualiza la página para mostrar la nueva vista

    destinations = [
        {"route": "/inicio", "icon": ft.icons.STAR, "label": "Principal"},
        {"route": "/graficos", "icon": ft.icons.STACKED_BAR_CHART, "label": "Gráficos"},
        {"route": "/configuracion", "icon": ft.icons.SETTINGS, "label": "Configuración"}
    ]
    
    nav_rail = NavigationRailClass(handle_route_change, destinations, page)

    def grafico_desempeno_view():
        df = obtener_datos_para_grafico()
        fig = crear_figura_plotly(df)
        grafico = PlotlyChart(fig, expand=True)
        return grafico

    def route_change(e):
        if page.route == "/inicio":
            login_screen = ButtonScreen(handle_route_change, nav_rail, page)
            page.views.clear()
            page.views.append(ft.View("/inicio", controls=[login_screen.render()], bgcolor="#1f262f"))
        elif page.route == "/graficos":
            grafico_screen = grafico_desempeno_view()
            page.views.clear()
            page.views.append(ft.View("/graficos", controls=[grafico_screen], bgcolor="#1f262f"))
        page.update()

    page.on_route_change = route_change
    page.go("/inicio")

ft.app(target=main, view=ft.AppView.FLET_APP)
