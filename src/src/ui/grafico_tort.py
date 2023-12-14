import sqlite3
import pandas as pd
import flet as ft

DATABASE_PATH = 'data/estudiantes.db'

class GraphTort():

    def obtener_datos_para_grafico(self):
        # Realiza la conexión a la base de datos y obtén los datos
        conn = sqlite3.connect(DATABASE_PATH)
        query = """
            SELECT semestre, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM estudiantes) as porcentaje
            FROM estudiantes
            GROUP BY semestre;
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    def build(self):
        df = self.obtener_datos_para_grafico()

        chart_sections = []
        for _, row in df.iterrows():
            section = ft.PieChartSection(
                value=row['porcentaje'],
                title=f"{row['porcentaje']:.2f}%",
                title_style=ft.TextStyle(size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                color=ft.colors.BLUE,  # Aquí podrías asignar colores diferentes para cada sección si lo deseas
                radius=50
            )
            chart_sections.append(section)

        chart = ft.PieChart(
            sections=chart_sections,
            sections_space=0,
            center_space_radius=40,
            expand=True
        )
        return ft.Row(
            [
                chart_sections,
                ft.VerticalDivider(width=3),
                chart,  
            ],
            width=700,
            height=700,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )


