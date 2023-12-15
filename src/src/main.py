import flet as ft
from flet.plotly_chart import PlotlyChart
from widgets.nav import NavigationRailClass
from ui.grafico_line import GraphScreen

def main(page: ft.Page):

    page.title = "Routes Example"

    async def handle_route_change(route):
        page.go_async(route)

    destinations = [
    {"route": "/graficos", "icon": ft.icons.SHOW_CHART, "label": "Gráficos"},
    {"route": "/proyeccion", "icon": ft.icons.TIMELINE, "label": "Proyección Curricular"},
    ]

    nav_rail = NavigationRailClass(handle_route_change, destinations, page)
    navigation_rail = nav_rail.create_rail()
    page.add(navigation_rail)


    def route_change(e):
        if page.route == "/graficos":
            graph_line = GraphScreen(handle_route_change, nav_rail)
            page.views.clear()
            page.views.append(ft.View("/graficos", controls=[graph_line.build()], bgcolor='#0E3039'))
            
        elif page.route == "/proyeccion":
            proyeccion_controls = []
            page.views.clear()
            page.views.append(ft.View("/proyeccion", controls=proyeccion_controls, bgcolor='#0E3039'))
        page.update()

    
    page.on_route_change = route_change
    page.go("/graficos")

ft.app(target=main, view=ft.AppView.FLET_APP)
