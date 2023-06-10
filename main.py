"""
    Universitat de Barcelona
    Título TFG: Evaluación automática de programas en python a partir de árboles de sintaxis abstracta.
    Autora: Estela Pérez Bassedas
    Fecha: 13/06/2023

    Ejemplos de argumentos para ejecutar este código en Python:
    * function_name = "subcadena_mes_llarga"
    * submissions_path = 'Datos/Entregas_alumnos'
    * solution_path = 'Datos/Solución_profesor.ipynb'
    * student_evaluation = "Datos/Calificaciones_profesor_lab8.ods"
    * results_directory_name = "Resultados"
    * num_col_name = 1
    * num_col_surname = 0
    * num_col_evaluation = 3

    Comando ejemplo para ejecutar este código de Python:
    python main.py "subcadena_mes_llarga" "Datos/Entregas_alumnos" "Datos/Solución_profesor.ipynb"
    "Datos/Calificaciones_profesor_lab8.ods" 1 0 3
"""

import argparse

from Funciones.ast_processing import *
from Funciones.distance_processing import *
from Funciones.results_processing import *


# Realiza un procesamiento de las entregas de estudiantes y genera resultados basados en las evaluaciones
# manuales de estas entregas.
def main(function_name, submissions_path, solution_path, student_evaluation, num_col_name, num_col_surname,
         num_col_evaluation):

    results_directory_name = "Resultados"
    results_directory_path = results_directory_name + "/resultados.csv"
    table_directory_path = results_directory_name + "/tabla_resultados.html"
    results = []

    students_evaluation = get_students_evaluation(student_evaluation, num_col_name, num_col_surname, num_col_evaluation)
    ast_solution = get_ast_from_code_cell(solution_path, function_name)

    # Recorre los directorios del path donde se encuentran las entregas de los alumnos e iteramos a traves de los
    # archivos de cada directorio localizando el Notebook de Jupyter (.ipynb).
    for root, directories, files in os.walk(submissions_path):
        for archive in files:
            if archive.endswith('.ipynb'):
                file_path = os.path.join(root, archive)                        # Obtenemos la ruta completa del archivo
                student_name = get_student_name(file_path)                         # Obtenemos el nombre del estudiante
                evaluation = students_evaluation.get(unidecode(student_name), '')  # Obtenemos nota del estudiante
                try:
                    ast_student = get_ast_student(file_path, function_name, student_name)
                    distance, counters = calculate_distance(ast_student, ast_solution)
                    normalized_distance = normalized_tree_edit_distance(counters[0], counters[1], distance)
                    results.append((student_name, distance, evaluation, normalized_distance))
                except Exception:
                    results.append((student_name, "Error", evaluation, None))

    writer_results_to_csv(results, results_directory_path)
    calculate_correlation(results_directory_path)
    create_table_html_for_compare_results(results_directory_path, table_directory_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name', help='Nombre de la función a evaluar')
    parser.add_argument('submissions_path', help='Path del directorio que contiene las entregas de los alumnos')
    parser.add_argument('solution_path', help='Path del archivo con la solución de referencia')
    parser.add_argument('student_evaluation', help='Path del archivo csv que contiene las evaluaciones manuales de '
                                                   'los alumnos')

    parser.add_argument('num_col_name', type=int, help='Número de la columna que corresponde al nombre dentro del '
                                                       'archivo excel que contiene la evalución manual del estudiante')
    parser.add_argument('num_col_surname', type=int, help='Número de la columna que corresponde al apellido dentro '
                                                          'del archivo excel que contiene la evalución manual del '
                                                          'estudiante')
    parser.add_argument('num_col_evaluation', type=int, help='Número de la columna que corresponde a la nota dentro '
                                                             'del archivo excel que contiene la evalución manual del '
                                                             'estudiante')

    args = parser.parse_args()
    main(args.function_name, args.submissions_path, args.solution_path, args.student_evaluation,
         args.num_col_name, args.num_col_surname, args.num_col_evaluation)
