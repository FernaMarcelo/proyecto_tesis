import sqlite3
import pandas as pd
import plotly.express as px
import flet as ft
from flet.plotly_chart import PlotlyChart

# Asegúrate de que esta ruta sea correcta para tu archivo de base de datos
DATABASE_PATH = 'data/estudiantes.db'

class graph_screen(ft.UserControl):
    
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




        # Obtener DataFrame con los datos
        df = self.obtener_datos_para_grafico()
        
        # Asegúrate de que la columna 'fecha_ingreso' sea tratada como un número entero, ya que solo contiene el año
        df['fecha_ingreso'] = df['fecha_ingreso'].astype(int)

        # Crear el gráfico con Plotly
        fig = px.bar(df, x="fecha_ingreso", y="IDPS", color="Alumno", title="Índice de Desempeño Promedio del Semestre (IDPS) por Año de Ingreso")

        # Agregar el gráfico de Plotly a la página de Flet
        page.add(PlotlyChart(fig, expand=True))
