import sqlite3


class BD():
    def __init__(self):
        pass

        
    def create_connection(self,db_file):
        """ Crea una conexión a la base de datos SQLite especificada por db_file """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

        return conn

    def create_table(self,conn, create_table_sql):
        """ Crea una tabla usando el create_table_sql proporcionado """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
        

    def _initialize_database(self):
        database = r"data\estudiantes.db"

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
        
        # Crear conexión a la base de datos
        conn = self.create_connection(database)

        # Crear tabla
        if conn is not None:
            self.create_table(conn, sql_create_estudiantes_table)
            self.create_table(conn, sql_create_cursos_table)
            self.create_table(conn, sql_create_notas_table)
            conn.close()
        else:
            print("Error! No se pudo crear la conexión a la base de datos.")

if __name__ == '__main__':
    bd = BD()
    bd._initialize_database()