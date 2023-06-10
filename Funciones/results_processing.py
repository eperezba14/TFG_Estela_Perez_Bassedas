import csv
import os
import ezodf
import matplotlib.pyplot as plt
import pandas as pd
from unidecode import unidecode


def get_students_evaluation(file_real_score_name, num_col_name, num_col_surname, num_col_real_score):

    # Abre el archivo que contiene las calificaciones manuales y obtiene la primera hoja del archivo.
    doc = ezodf.opendoc(file_real_score_name)
    sheet = doc.sheets[0]
    df_dict = {}

    # Recorremos las filas de la hoja, si es la primera fila (encabezados) continuamos el siguiente ciclo, en cuanto la
    # fila no es nula recogemos los datos y los guardamos (nombre, nota manual y nombre estudiante)
    for i, row in enumerate(sheet.rows()):
        if i == 0:
            continue
        if row[0].value is not None:
            name = (row[num_col_surname].value + " " + row[num_col_name].value).upper()
            real_score = row[num_col_real_score].value
            name_unidecode = unidecode(get_formatted_name(name)).strip()  # Quito los acentos
            df_dict[name_unidecode] = real_score
    return df_dict


def calculate_correlation(results_directory_path):

    # Se leen los datos del archivo CSV y después cojo las columnas 'Predicted_score' y 'Reference_score'.
    datos = pd.read_csv(results_directory_path, sep=',', encoding="latin-1")
    x = datos['Puntuación_predicha']
    y = datos['Puntuación_referencia']

    # Cálculo de la correlación
    correlation = x.corr(y)

    # Creamos el diagrama de dispersión, añadiéndole el valor de correlación obtenido y lo guardamos como png.
    plt.scatter(x, y, color='purple')
    plt.title('Diagrama de dispersión entre puntuación predicha y de referencia')
    plt.xlabel('Puntuación predicha')
    plt.ylabel('Puntuación de referencia')
    plt.annotate('Correlación: {:.3f}'.format(correlation), xy=(1, -0.1), xycoords='axes fraction',
                 fontsize=10, ha='right', va='top', bbox=dict(facecolor='white', edgecolor='None', alpha=0.7))
    plt.savefig('Resultados/Diagrama_dispersión.png')


def writer_results_to_csv(results: list, results_directory_path):

    # Verificamos si la carpeta 'result_directory' existe, si no existe la creamos.
    directory_results = os.path.dirname(results_directory_path)
    if not os.path.exists(directory_results):
        os.makedirs(directory_results)

    # Se crea o modifica el archivo CSV con los resultados que se han ido obteniendo
    with open(results_directory_path, "w", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(
            ["Nombre_estudiante", "Distancia", "Puntuación_referencia", "Puntuación_predicha"]
        )
        for result in results:
            writer.writerow(result)


def create_table_html_for_compare_results(results_directory_path, table_directory_path):

    df = pd.read_csv(results_directory_path, sep=',', encoding="latin-1")
    df.to_html(table_directory_path, index=False, encoding="latin-1", header=True, table_id='tabla',
               classes='table table-striped')

    # Obtener el directorio actual
    current_directory = os.getcwd()
    # Combinar el directorio actual con la ruta del archivo HTML
    html_file_path = os.path.join(current_directory, table_directory_path)
    # Abrir el archivo HTML en el navegador predeterminado
    os.startfile(html_file_path)


# Función que obtiene el nombre del alumno cogiendo el nombre del directorio a través de su path.
def get_student_name(file_path):
    parts = file_path.split("\\")
    student_name = parts[1].split("_")[0].upper()
    return get_formatted_name(student_name)


# Para controlar los espacios entre palabras y los acentos. Dividimos la cadena "X X X" en palabras ["X", "X", "X"] y
# por último retornamos una nueva cadena uniendo las palabras, que tienen 1 espacio entre ellas.
def get_formatted_name(name):
    student_name_comparable = name.split()
    return " ".join(student_name_comparable).replace("'", "")
