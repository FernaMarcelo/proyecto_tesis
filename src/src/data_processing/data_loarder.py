import pandas as pd
import sqlite3

# Asumiendo que el archivo Excel está en la carpeta 'data'
excel_path = r'C:\Users\xmarc\OneDrive\Documentos\GitHub\proyecto\data\CAPP_Alumnos_por_Malla_Informatica_minu.xlsx'
requisitos_excel_path = r'C:\Users\xmarc\Downloads\CATALOGO DE CURSO ING INFORMATICA 05-10-22 malla antigua.xlsx'


def load_data(excel_path):
    # Leer el archivo Excel
    df = pd.read_excel(excel_path, engine='openpyxl')

    # Realizar cualquier limpieza de datos o preprocesamiento si es necesario
    # Por ejemplo, podrías querer convertir las fechas a un formato estándar
    # o manejar los valores 'AC' en las notas como NaN o un valor específico

    return df

def load_requisitos(excel_path):
    # Leer el archivo Excel con los requisitos
    df = pd.read_excel(excel_path, engine='openpyxl')
    return df

def save_to_sqlite(df, db_path, table_name):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)

    # Guardar el DataFrame en la base de datos como la tabla especificada
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Cargar datos de estudiantes
    df_estudiantes = load_data(excel_path)
    # Guardar en SQLite en la tabla 'estudiantes'
    save_to_sqlite(df_estudiantes, r'data\estudiantes.db', 'estudiantes')
    
    # Cargar datos de requisitos
    df_requisitos = load_data(requisitos_excel_path)
    # Guardar en SQLite en la tabla 'requisitos'
    save_to_sqlite(df_requisitos, r'data\estudiantes.db', 'requisitos')


