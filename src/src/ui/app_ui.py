import sys
import os

# Esto agrega el directorio src al PYTHONPATH.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import flet as ft
import database

class State:
    toggle = True

s = State()

def obtener_datos_para_grafico():
    conn = database.create_connection(r'C:\Users\Tesis\Desktop\tesisMark1\data\estudiantes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM estudiantes")
    rows = cur.fetchall()
    conn.close()  # Es importante cerrar la conexión después de usarla.
    

        # Crear una serie de datos para cada ramo
    serie_ser_universitario = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_matematicas = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_quimica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_fundamentos_de_ingenieria = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_programacion = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_taller_habilidades_computacionales = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_acompanamiento_y_tutorias1 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_comunicacion_efectiva = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_calculo_diferencial = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_algebra = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_mecanica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_taller_ingenieria = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_programacion_avanzada = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_acompanamiento_y_tutorias2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_antropologia = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_calculo_integral = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_algebra_lineal = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_calor_y_ondas = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_microeconomia = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_bases_de_datos = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_acompanamiento_y_tutorias3 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_liderazgo_y_trabajo_en_equipo = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_calculo_vectorial = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_ecuaciones_diferenciales = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_contabilidad_gerencial = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_emprendimiento = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_estadistica_descriptiva_y_probabilidades = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_acompanamiento_y_tutorias4 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_etica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_creatidad = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_electronica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_matematicas_discreta = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_optimizacion = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_ingenieria_economica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_ingles5 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_senales_y_sistemas = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_arquitectura_de_computadores = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_algoritmos = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_inferencia_estadistica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_evaluacion_de_proyectos = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_ingles6 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_comunicaciones_digitales = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_redes_de_datos = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_sistemas_operativos = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_modelos_estocasticos = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_taller_emprendimiento = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_taller_profesional1 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_seguridad_informatica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_ingenieria_de_software = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_electivo_ing_informatica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_electivo_fac_informatica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_electivo2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_simulacion_de_sistemas = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_taller_profesional2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_ingenieria_de_sistemas = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_gestion_tics = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_electivo_doble_ing_informatica = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    # Crear una serie de datos para cada ramo
    serie_electivo_ing_informatica2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )

    serie_taller_herramientas = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[2]) for row in rows if row[2] is not None],
        stroke_width=2,
        color=ft.colors.BLUE,
    )

    serie_taller_innovacion_e_ingenieria = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_electivo_fac_informatica2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    serie_electivo_doble_ing_informatica2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_electivo_ing_informatica3 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    serie_taller_insercion_laboral = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_trabajo_titulacion = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    serie_ingles1 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_ingles2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    serie_ingles3 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_ingles4 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    serie_minor1 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[3]) for row in rows if row[3] is not None],
        stroke_width=2,
        color=ft.colors.RED,
    )
    serie_minor2 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    serie_minor3 = ft.LineChartData(
        data_points=[ft.LineChartDataPoint(x=row[0], y=row[1]) for row in rows if row[1] is not None],
        stroke_width=2,
        color=ft.colors.GREEN,
    )
    
    return [serie_ser_universitario, serie_matematicas, serie_quimica, serie_fundamentos_de_ingenieria, serie_programacion, serie_taller_habilidades_computacionales, serie_acompanamiento_y_tutorias1, serie_comunicacion_efectiva, serie_calculo_diferencial, serie_algebra, serie_mecanica, serie_taller_ingenieria, serie_programacion_avanzada, serie_acompanamiento_y_tutorias2, serie_antropologia, serie_calculo_integral, serie_algebra_lineal, serie_calor_y_ondas, serie_microeconomia, serie_bases_de_datos, serie_acompanamiento_y_tutorias3, serie_liderazgo_y_trabajo_en_equipo, serie_calculo_vectorial, serie_ecuaciones_diferenciales, serie_contabilidad_gerencial, serie_emprendimiento, serie_estadistica_descriptiva_y_probabilidades, serie_acompanamiento_y_tutorias4, serie_etica, serie_creatidad, serie_electronica, serie_matematicas_discreta, serie_optimizacion, serie_ingenieria_economica, serie_ingles5, serie_senales_y_sistemas, serie_arquitectura_de_computadores, serie_algoritmos, serie_inferencia_estadistica, serie_evaluacion_de_proyectos, serie_ingles6, serie_comunicaciones_digitales, serie_redes_de_datos, serie_sistemas_operativos, serie_modelos_estocasticos, serie_taller_emprendimiento, serie_taller_profesional1, serie_seguridad_informatica, serie_ingenieria_de_software, serie_electivo_ing_informatica, serie_electivo_fac_informatica, serie_electivo2, serie_simulacion_de_sistemas, serie_taller_profesional2, serie_ingenieria_de_sistemas, serie_gestion_tics, serie_electivo_doble_ing_informatica, serie_electivo_ing_informatica2, serie_taller_herramientas, serie_taller_innovacion_e_ingenieria, serie_electivo_fac_informatica2, serie_electivo_doble_ing_informatica2, serie_electivo_ing_informatica3, serie_taller_insercion_laboral, serie_trabajo_titulacion, serie_ingles1, serie_ingles2, serie_ingles3, serie_ingles4, serie_minor1, serie_minor2, serie_minor3]
    # Transformar los datos de las filas a LineChartData aquí.
    # Este es un ejemplo genérico y debes adaptarlo a tu esquema de datos.
    series = [
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x, y) for x, y in enumerate(row)],
            stroke_width=2,
            color=ft.colors.BLUE,
        ) for row in rows
    ]
    return series

def main(page: ft.Page):
    page.title = "Analisis de Estudiantes"

    # Llamar a la función para obtener los datos del gráfico
    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(x=1, y=1),
                ft.LineChartDataPoint(x=3, y=1.5),
                ft.LineChartDataPoint(x=5, y=1.4),
                ft.LineChartDataPoint(x=7, y=3.4),
                ft.LineChartDataPoint(x=10, y=2),
                ft.LineChartDataPoint(x=12, y=2.2),
                ft.LineChartDataPoint(x=13, y=1.8),
            ],
            stroke_width=4,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),

    
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(x=1, y=1),
                ft.LineChartDataPoint(x=3, y=2.8),
                ft.LineChartDataPoint(x=7, y=1.2),
                ft.LineChartDataPoint(x=10, y=2.8),
                ft.LineChartDataPoint(x=12, y=2.6),
                ft.LineChartDataPoint(x=13, y=3.9),
            ],
            color=ft.colors.PINK,
            below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
            stroke_width=4,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(x=1, y=2.8),
                ft.LineChartDataPoint(x=3, y=1.9),
                ft.LineChartDataPoint(x=6, y=3),
                ft.LineChartDataPoint(x=10, y=1.3),
                ft.LineChartDataPoint(x=13, y=2.5),
            ],
            color=ft.colors.CYAN,
            stroke_width=4,
            curved=True,
            stroke_cap_round=True,
        ),
    
    ]
    data_2 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(x=1, y=1),
                ft.LineChartDataPoint(x=3, y=4),
                ft.LineChartDataPoint(x=5, y=1.8),
                ft.LineChartDataPoint(x=7, y=5),
                ft.LineChartDataPoint(x=10, y=2),
                ft.LineChartDataPoint(x=12, y=2.2),
                ft.LineChartDataPoint(x=13, y=1.8),
            ],
            stroke_width=4,
            color=ft.colors.with_opacity(0.5, ft.colors.LIGHT_GREEN),
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(x=1, y=1),
                ft.LineChartDataPoint(x=3, y=2.8),
                ft.LineChartDataPoint(x=7, y=1.2),
                ft.LineChartDataPoint(x=10, y=2.8),
                ft.LineChartDataPoint(x=12, y=2.6),
                ft.LineChartDataPoint(x=13, y=3.9),
            ],
            color=ft.colors.with_opacity(0.5, ft.colors.PINK),
            below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.PINK),
            stroke_width=4,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(x=1, y=3.8),
                ft.LineChartDataPoint(x=3, y=1.9),
                ft.LineChartDataPoint(x=6, y=5),
                ft.LineChartDataPoint(x=10, y=3.3),
                ft.LineChartDataPoint(x=13, y=4.5),
            ],
            color=ft.colors.with_opacity(0.5, ft.colors.CYAN),
            stroke_width=4,
            stroke_cap_round=True,
        ),
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4,
                    label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        ft.Text(
                            "OCT",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "DEC",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=4,
        min_x=0,
        max_x=14,
        # animate=5000,
        expand=True,
    )

    # Función para alternar los datos del gráfico (puedes adaptarla a tus necesidades)
    def toggle_data(e):
        nonlocal chart
        # Aquí deberías cambiar la lógica para actualizar los datos basándote en tu aplicación real.
        # Esto es solo un ejemplo.
        if s.toggle:
            chart.data_series = data_2  # Suponiendo que quieres recargar los mismos datos.
        else:
            chart.data_series = data_1  # O cambiar a un conjunto de datos diferente.
        s.toggle = not s.toggle
        chart.update()

    # Agregar un botón para actualizar el gráfico y el gráfico a la página
    page.add(ft.IconButton(ft.icons.REFRESH, on_click=toggle_data), chart)

ft.app(target=main)