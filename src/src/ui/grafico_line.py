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
    
    def obtener_datos_para_grafico_tort(self):
        # Realiza la conexión a la base de datos y obtén los datos
        conn = sqlite3.connect(DATABASE_PATH)
        query = """
            WITH YearlyCounts AS (
            SELECT 
            CAST(SUBSTR(fecha_ingreso, 1, 4) AS INTEGER) AS Year, 
            COUNT(*) AS Quantity
            FROM estudiantes
            WHERE fecha_ingreso IS NOT NULL AND fecha_ingreso != 'NaN'
            GROUP BY Year
            ORDER BY Year
            ),
            YearlyDifferences AS (
            SELECT 
            Year, 
            Quantity,
            Quantity - LAG(Quantity, 1, 0) OVER (ORDER BY Year) AS Change
            FROM YearlyCounts
            )
            SELECT Year, Quantity, Change FROM YearlyDifferences;
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    
    def crear_figura_plotly_con_datos_torta(self, df):
        # Asegúrate de que las columnas sean tratadas como números enteros
        df['Year'] = df['Year'].astype(int)
        df['Quantity'] = df['Quantity'].astype(int)
        df['Change'] = df['Change'].astype(int)

        # Crear el gráfico con Plotly
        fig = px.bar(df, x="Year", y="Quantity", text="Change", 
                     title="Cantidad en aumento de Estudiantes por Año de Ingreso")
        return fig

    def build(self):
        rail = self.nav_rail_class.create_rail()

        # Gráfico de barras original
        df = self.obtener_datos_para_grafico()
        fig1 = self.crear_figura_plotly(df)
        grafico1 = PlotlyChart(figure=fig1, expand=True)

        # Nuevo gráfico de barras usando los datos del gráfico de torta
        df_tort = self.obtener_datos_para_grafico_tort()
        fig2 = self.crear_figura_plotly_con_datos_torta(df_tort)
        grafico2 = PlotlyChart(figure=fig2, expand=True)
    


        return ft.Column(
            [
                rail,
                ft.Row(
                    [
                        grafico1,
                        grafico2
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            ],
            alignment=ft.MainAxisAlignment.START,  
            
                  
        )
