import sqlite3


class BD():
    def __init__(self):
        self.database = r"data\estudiantes.db"
        self.conn = self.create_connection(self.database)
        self._initialize_database()

        
    def create_connection(self, db_file):
        """ Create a database connection to the SQLite database specified by db_file """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return None
        
    def create_table(self, create_table_sql):
        """ Create a table using the create_table_sql provided """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def _initialize_database(self):

         # Creación de la tabla de cursos
        sql_create_cursos_table = """ CREATE TABLE IF NOT EXISTS Cursos (
                                        id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre_curso TEXT NOT NULL,
                                        codigo_curso TEXT NOT NULL,
                                        semestre INTEGER NOT NULL
                                    ); """

        sql_create_estudiantes_table = """ CREATE TABLE IF NOT EXISTS estudiantes (
                                            Alumno integer PRIMARY KEY,
                                            fecha_ingreso text NOT NULL,
                                            ser_universitario real,
                                            matematicas real,
                                            quimica real,
                                            fundamentos_de_ingenieria real,
                                            programacion real,
                                            taller_habilidades_computacion real,
                                            acompanamiento_y_tutorias1 real, 
                                            comunicacion_efectiva real, 
                                            calculo_diferencial real, 
                                            algebra TEXT, mecanica real, 
                                            taller_ingenieria real, 
                                            programacion_avanzada real, 
                                            acompanamiento_y_tutorias2 real, 
                                            antropologia real, 
                                            calculo_integral real,
                                            algebra_lineal real, 
                                            calor_y_ondas real, 
                                            microeconomia real, 
                                            bases_de_datos real, 
                                            acompanamiento_y_tutorias3 real, 
                                            liderazgo_y_trabajo_en_equipo real, 
                                            calculo_vectorial real, 
                                            ecuaciones_diferenciales real, 
                                            contabilidad_gerencial real, 
                                            emprendimiento real, 
                                            estadistica_descriptiva_y_probabilidades real, 
                                            acompanamiento_y_tutorias4 real, 
                                            etica real, 
                                            creatividad real, 
                                            electronica real, 
                                            matematicas_discreta real, 
                                            optimizacion real, 
                                            ingenieria_economica real, 
                                            ingles5 real, 
                                            senales_y_sistemas real, 
                                            arquitectura_de_computadores real, 
                                            algoritmos real, 
                                            inferencia_estadistica real, 
                                            evaluacion_de_proyectos real, 
                                            ingles6 real, 
                                            comunicaciones_digitales real, 
                                            redes_de_datos real, 
                                            sistemas_operativos real, 
                                            modelos_estocasticos real, 
                                            taller_emprendimiento real, 
                                            taller_profesional1 real, 
                                            seguridad_informatica real, 
                                            ingenieria_de_software real, 
                                            electivo_ing_informatica real, 
                                            electivo_fac_informatica real, 
                                            electivo2 real, 
                                            simulacion_de_sistemas real, 
                                            taller_profesional2 real, 
                                            ingenieria_de_sistemas real, 
                                            gestion_tics real, 
                                            electivo_doble_ing_informatica real,
                                            electivo_ing_informatica2 real, 
                                            taller_herramientas real, 
                                            taller_innovacion_e_ingenieria real, 
                                            electivo_fac_informatica2 real, 
                                            electivo_ing_informatica3 real, 
                                            taller_insercion_laboral real, 
                                            trabajo_titulacion real, 
                                            ingles1 real, 
                                            ingles2 real, 
                                            ingles3 real, 
                                            ingles4 real, 
                                            minor1 real, 
                                            minor2 real, 
                                            minor3 real 
                                        
                                    ); """
        
        # Creación de la tabla de notas
        sql_create_notas_table = """ CREATE TABLE IF NOT EXISTS Notas (
                                        id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
                                        id_estudiante INTEGER,
                                        id_curso INTEGER,
                                        nota REAL,
                                        FOREIGN KEY (id_estudiante) REFERENCES Estudiantes (id_estudiante),
                                        FOREIGN KEY (id_curso) REFERENCES Cursos (id_curso)
                                    ); """
        
        # Crear tabla para requisitos si no existe
        create_requisitos_sql = """ CREATE TABLE IF NOT EXISTS Requisitos (
                                    id_requisito INTEGER PRIMARY KEY AUTOINCREMENT,
                                    codigo_programa TEXT,
                                    codigo_curso TEXT NOT NULL,
                                    asignatura TEXT,
                                    tipo_asignatura TEXT,
                                    semestre TEXT,
                                    creditos INTEGER,
                                    creditos_corregidos INTEGER,
                                    numero_idoneo_alumno_profesor_modulo_teorico INTEGER,
                                    numero_maximo_alumnos_por_profesor INTEGER,
                                    modulos_teoricos_en_sala INTEGER,
                                    laboratorio INTEGER,
                                    taller INTEGER,
                                    simulacion INTEGER,
                                    practica_campus_clinico INTEGER,
                                    tutoria_mentoria INTEGER,
                                    suma_total_modulos_practicos INTEGER,
                                    ayudantia INTEGER,
                                    total_modulos INTEGER,
                                    numero_idoneo_alumnos_profesor_modulo_practico INTEGER,
                                    prerrequisitos TEXT,
                                    correquisitos TEXT,
                                    atributos TEXT,
                                    nombre_largo_curso TEXT,
                                    FOREIGN KEY (codigo_curso) REFERENCES Cursos (codigo_curso)
                                    ); """  # Completa con la estructura de tu tabla de requisitos
        
        # Execute table creation
        self.create_table(sql_create_cursos_table)
        self.create_table(sql_create_estudiantes_table)
        self.create_table(sql_create_notas_table)
        self.create_table(create_requisitos_sql)


    def get_student_grades(self, student_id):
        """Retrieve the grades for a specific student from the database."""
        cursor = self.conn.cursor()
        query = f"""
        SELECT * FROM estudiantes WHERE Alumno = ?
        """
        cursor.execute(query, (student_id,))
        row = cursor.fetchone()
        return row

    def get_course_requirements(self):
        """Retrieve the course requirements from the database."""
        cursor = self.conn.cursor()
        query = """
        SELECT codigo_curso, prerrequisitos FROM Requisitos
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return {row[0]: row[1].split(',') if row[1] else [] for row in rows}
    

    def close_connection(self):
        """ Close the database connection """
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    bd = BD()
    bd.close_connection()