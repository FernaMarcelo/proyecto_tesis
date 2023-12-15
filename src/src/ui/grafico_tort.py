import sqlite3
import pandas as pd
import flet as ft

DATABASE_PATH = 'data/estudiantes.db'

class GraphTort(ft.UserControl):  
    def __init__(self, route_change_handler, nav_rail_class, nav_rail):
        super().__init__()
        self.nav_rail = nav_rail
        self.route_change_handler = route_change_handler
        self.nav_rail_class = nav_rail_class
    

    def obtener_datos_para_grafico(self):
        # Realiza la conexión a la base de datos y obtén los datos
        conn = sqlite3.connect(DATABASE_PATH)
        query = """
            SELECT substr(fecha_ingreso, 1, 4) as ano, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM estudiantes) as porcentaje
            FROM estudiantes
            GROUP BY ano;
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    def build(self):
        df = self.obtener_datos_para_grafico()

        chart_sections = []
        # Paleta de colores para las secciones del gráfico
        colors = [ft.colors.RED, ft.colors.BLUE, ft.colors.GREEN, ft.colors.YELLOW, ft.colors.PURPLE]

        for index, row in df.iterrows():
            color = colors[index % len(colors)]  # Elige un color de la paleta
            section = ft.PieChartSection(
                value=row['porcentaje'],
                title=f"{row['ano']}: {row['porcentaje']:.2f}%",
                title_style=ft.TextStyle(size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                color=color,
                radius=50
            )
            chart_sections.append(section)

        chart = ft.PieChart(
            sections=chart_sections,
            sections_space=0,
            center_space_radius=40,
            expand=True
        )

        # Asegúrate de que el nav_rail esté correctamente configurado
        rail = self.nav_rail_class.create_rail()
        
        return ft.Row(
            [
                rail,
                ft.VerticalDivider(width=3),
                chart,  
            ],
            width=900,
            height=900,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )


