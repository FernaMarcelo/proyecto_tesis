import sqlite3
import pandas as pd
import plotly.express as px
import flet as ft
from flet.plotly_chart import PlotlyChart

# Asegúrate de que esta ruta sea correcta para tu archivo de base de datos
DATABASE_PATH = 'data/estudiantes.db'

class GraphScreen(ft.UserControl):
    def __init__(self, route_change_handler, nav_rail_class):
        super().__init__()
        self.route_change_handler = route_change_handler
        self.nav_rail_class = nav_rail_class
    
    def obtener_datos_para_grafico(self):
        conn = sqlite3.connect(DATABASE_PATH)
        query = "SELECT Alumno, fecha_ingreso, matematicas, quimica, fundamentos_de_ingenieria, programacion FROM estudiantes"
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Limpieza de datos: reemplaza 'NULL', valores vacíos o cualquier otro placeholder por NaN
        df.replace(['NULL', '', ' ', 'AC'], pd.NA, inplace=True)

        # Convertir las columnas de notas a numéricas
        columns_to_average = ['matematicas', 'quimica', 'fundamentos_de_ingenieria', 'programacion']
        df[columns_to_average] = df[columns_to_average].apply(pd.to_numeric, errors='coerce')

        # Eliminar filas donde 'fecha_ingreso' es NaN antes de la conversión a entero
        df.dropna(subset=['fecha_ingreso'], inplace=True)

        # Convertir la columna 'fecha_ingreso' a entero
        df['fecha_ingreso'] = df['fecha_ingreso'].astype(int)

        # Cálculo del promedio para el IDPS
        df['IDPS'] = df[columns_to_average].mean(axis=1)
        
        return df

    def crear_figura_plotly(self,df):
        # Asegúrate de que la columna 'fecha_ingreso' sea tratada como un número entero
        df['fecha_ingreso'] = df['fecha_ingreso'].astype(int)

        # Crear el gráfico con Plotly
        fig = px.bar(df, x="fecha_ingreso", y="IDPS", color="Alumno", title="Índice de Desempeño Promedio del Semestre (IDPS) por Año de Ingreso")
        return fig


    def build(self):
        rail = self.nav_rail_class.create_rail()
        title = ft.Text('Aquí están los graficos', size=24)
    


        return ft.Row(
            [
                rail,
                ft.VerticalDivider(width=3),
                
            ],
            width=800,
            height=800,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
