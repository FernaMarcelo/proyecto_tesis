import pandas as pd
import sqlite3

# Asumiendo que el archivo Excel está en la carpeta 'data'
excel_path = r'C:\Users\xmarc\OneDrive\Documentos\GitHub\proyecto\data\CAPP_Alumnos_por_Malla_Informatica_minu.xlsx'



def load_data(excel_path):
    # Leer el archivo Excel
    df = pd.read_excel(excel_path, engine='openpyxl')

    # Realizar cualquier limpieza de datos o preprocesamiento si es necesario
    # Por ejemplo, podrías querer convertir las fechas a un formato estándar
    # o manejar los valores 'AC' en las notas como NaN o un valor específico

    return df

def save_to_sqlite(df, db_path):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)

    # Guardar el DataFrame en la base de datos como una tabla llamada 'estudiantes'
    df.to_sql('estudiantes', conn, if_exists='replace', index=False)

    # Cerrar la conexión
    conn.close()

if __name__ == '__main__':
    # Cargar datos
    dataframe = load_data(excel_path)

    # Guardar en SQLite
    save_to_sqlite(dataframe, r'estudiantes.db')

