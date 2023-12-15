import sqlite3
import pandas as pd

DATABASE_PATH = 'data/estudiantes.db'

class DatabaseAnalysis:
    def __init__(self):
        self.conn = self.create_connection(DATABASE_PATH)

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return None

    def calculate_reprobation_rate(self):
        # Asumiendo que tienes una manera de unir las tablas estudiantes y cursos
        # y que puedes determinar qué nota significa reprobación.
        reprobation_query = """
        SELECT c.semestre, COUNT(DISTINCT e.alumno) as reprobados
        FROM estudiantes e
        JOIN cursos c ON e.matematicas_id_curso = c.id_curso
        WHERE e.matematicas < 4 OR e.quimica < 4 OR e.fundamentos_de_ingenieria < 4 OR e.programacion < 4
        GROUP BY c.semestre;

        """

        total_students_query = """
        SELECT c.semestre, COUNT(e.alumno) as total
        FROM estudiantes e
        JOIN cursos c ON e.matematicas_id_curso = c.id_curso -- y así sucesivamente para todos los cursos
        GROUP BY c.semestre;
        """

        # Ejecutar consultas y obtener DataFrames
        df_reprobation = pd.read_sql_query(reprobation_query, self.conn)
        df_total_students = pd.read_sql_query(total_students_query, self.conn)

        # Combinar los DataFrames en base al semestre
        df = pd.merge(df_reprobation, df_total_students, on='semestre')

        # Calcular la tasa de reprobación
        df['tasa_reprobacion'] = (df['reprobados'] / df['total']) * 100
        return df

    def close_connection(self):
        if self.conn:
            self.conn.close()

# Uso de la clase
db_analysis = DatabaseAnalysis()
df_rates = db_analysis.calculate_reprobation_rate()
db_analysis.close_connection()
