# widgets/nav.py
import flet as ft
import asyncio


class NavigationRailClass:
    def __init__(self, route_change_handler, destinations, page, selected_index=0):
        self.route_change_handler = route_change_handler
        self.destinations = destinations
        self.page = page
        self.selected_index = selected_index

    def on_change(self, event):
        index = event.control.selected_index
        if 0 <= index < len(self.destinations):
            selected_route = self.destinations[index]["route"]
            # Obtener la ruta actual
            current_route = self.page.route

            # print(f"selected_route :{selected_route}")
            # print(f"current_route :{current_route}")
            if selected_route != current_route:
                self.set_selected_index(index)
                self.route_change_handler(selected_route)
               # print(f"Vistas Actuales: {[view.route for view in self.page.views]}")


                if len(self.page.views) > 1:
               
         
                    self.page.views.pop()
                else:
                    # Si hay 2 o menos vistas, no eliminar ninguna
                    print(
                        "No se elimina ninguna vista. Manteniendo {selected_route}.")

                self.route_change_handler(selected_route)
            else:
                print(
                    "La ruta seleccionada es la misma que la ruta actual. No se realiza ninguna acción.")
        else:
            print(f"Índice fuera de rango: {index}")

    def set_selected_index(self, index):
        self.selected_index = index
        self.page.update()

    def create_rail(self):
        rail_destinations = []
        for i, destination in enumerate(self.destinations):

            rail_destinations.append(
                ft.NavigationRailDestination(
                    icon=destination["icon"],
                    selected_icon=destination.get(
                        "selected_icon", destination["icon"]),
                    label=destination.get("label", ""),

                )
            )

        rail = ft.NavigationRail(
            selected_index=self.selected_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=56,
            min_extended_width=100,
            group_alignment=-0.9,
            height=150,
            destinations=rail_destinations,
            on_change=self.on_change,
            disabled=False,
        )
        return rail
