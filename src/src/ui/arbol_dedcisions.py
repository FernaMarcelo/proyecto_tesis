import pandas as pd

# Asumiendo que ya tienes un DataFrame con las notas de los estudiantes por cada curso.
# Las notas pueden estar en un rango de 0.0 a 7.0, con NaN indicando que no se ha tomado el curso.

# Cargar las notas y los prerrequisitos de los estudiantes desde la base de datos o un archivo Excel.
# Este es un ejemplo simplificado con datos ficticios.

notas_data = {
    'alumno_id': [1, 1, 2, 2],
    'curso_codigo': ['CURSO1', 'CURSO2', 'CURSO1', 'CURSO2'],
    'nota': [6.0, None, 5.5, None],
    'prerrequisitos_cumplidos': [True, False, True, False]
}

df_notas = pd.DataFrame(notas_data)

# Asumiendo que tienes un grafo de prerrequisitos construido previamente.
# Aquí usamos un diccionario simple para simular los prerrequisitos.

prerrequisitos = {
    'CURSO2': ['CURSO1'],  # CURSO1 es prerrequisito de CURSO2
    # Añade aquí el resto de los prerrequisitos de cursos
}

# Función para determinar los cursos que el alumno puede cursar
def cursos_disponibles_para_alumno(df_notas, alumno_id, prerrequisitos):
    # Obtener los cursos que el alumno ha pasado
    cursos_aprobados = df_notas[(df_notas['alumno_id'] == alumno_id) & (df_notas['nota'] >= 4.0)]['curso_codigo'].tolist()

    # Determinar los cursos disponibles basados en los prerrequisitos
    cursos_disponibles = []
    for curso, prereqs in prerrequisitos.items():
        if all(prereq in cursos_aprobados for prereq in prereqs):
            # Verificar si el alumno ya ha tomado el curso
            if curso not in cursos_aprobados and pd.isna(df_notas[(df_notas['alumno_id'] == alumno_id) & (df_notas['curso_codigo'] == curso)]['nota']).any():
                cursos_disponibles.append(curso)
    
    return cursos_disponibles

# Ejemplo de uso para un alumno con ID 1
cursos_para_alumno_1 = cursos_disponibles_para_alumno(df_notas, 1, prerrequisitos)
print(f'Cursos disponibles para el alumno 1: {cursos_para_alumno_1}')
