import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from src.database.database import BD

# Asumiendo que 'requisitos_excel_path' es la ruta a tu archivo Excel
requisitos_excel_path = os.path.join(os.getcwd(), 'data', 'CATALOGO DE CURSO ING INFORMATICA 05-10-22 malla antigua.xlsx')
# Asumiendo que 'notas_excel_path' es la ruta a tu archivo Excel con las notas de los alumnos
notas_excel_path = os.path.join(os.getcwd(), 'data', 'CAPP_Alumnos_por_Malla_Informatica_minu.xlsx')

class Grafo:
    def __init__(self, database_connection):
        self.db = database_connection
        self.df_requisitos = self.db.get_course_requirements()
        self.G = self.build_prerequisite_graph(self.df_requisitos)


    @staticmethod
    def load_requisitos(excel_path):
        df = pd.read_excel(excel_path, header=2)
        # Imprime los nombres de las columnas para verificar si 'prerrequisitos' está presente
        print(df.columns)
        # Asegúrate de que 'prerrequisitos' sea uno de los nombres de las columnas
        if 'prerrequisitos' in df.columns:
            df['prerrequisitos'] = df['prerrequisitos'].apply(
                lambda x: x.split(',') if pd.notnull(x) else []
            )
        else:
            raise KeyError("La columna 'prerrequisitos' no se encuentra en el DataFrame.")
        return df



    @staticmethod
    def build_prerequisite_graph(course_requirements):
        G = nx.DiGraph()
        for course, prerequisites in course_requirements.items():
            G.add_node(course)
            for prereq in prerequisites:
                G.add_node(prereq)
                G.add_edge(prereq, course)
        return G


    def visualize_student_progress(self, student_id):
        # Obtener las notas del estudiante de la base de datos
        student_grades_row = self.db.get_student_grades(student_id)
        # Convertir a un diccionario para facilitar el acceso
        student_grades = {self.G.nodes[i]['codigo_curso']: grade for i, grade in enumerate(student_grades_row) if grade is not None}
        # Identifica los cursos completados, en progreso y no iniciados
        passed_courses = student_grades[student_grades >= 4.0].dropna().index.tolist()
        in_progress_courses = student_grades[student_grades.isna()].index.tolist()

        # Define los colores de los nodos
        color_map = ['green' if node in passed_courses else 'orange' if node in in_progress_courses else 'grey' for node in self.G]

        # Visualiza el grafo
        plt.figure(figsize=(20, 20))
        pos = nx.kamada_kawai_layout(self.G)
        nx.draw(self.G, pos, node_color=color_map, with_labels=True, edge_color='black',
                node_size=[len(self.G.in_edges(n)) * 100 for n in self.G.nodes()],
                font_size=8)
        plt.title(f'Progreso del Alumno {student_id}')
        plt.savefig(f'progreso_alumno_{student_id}.png')
        plt.show()

# Puntos de entrada para ejecutar el código
if __name__ == "__main__":
    database_connection = BD()
    grafo = Grafo(database_connection)
    student_id = 1  # El ID del alumno que quieres visualizar
    grafo.visualize_student_progress(student_id)