import ast
import os
import nbformat
from zss import Node


# Recorre el directorio pasado como argumento, y por cada notebook de jupyter cogemos la celda de código que contiene
# la función con el nombre pasado como argumento y genera su AST. Retornamos una lista con el AST de cada código
# solución que haya en el directorio.
def get_asts_solutions(solutions_directory_path, function_name):
    ast_solutions = []
    for root, directories, files in os.walk(solutions_directory_path):
        for archivo in files:
            if archivo.endswith('.ipynb'):
                file_path = os.path.join(root, archivo)
                try:
                    ast_solution = get_ast_from_code_cell(file_path, function_name)
                except Exception as error:
                    ast_solution = error
                ast_solutions.append(ast_solution)
    return ast_solutions


# Intenta obtener el AST del código de una celda en el archivo utilizando la llamada a una función, en caso de algun
# error se muestra un mensaje de error.
def get_ast_student(ruta_archivo: str, nombre_funcion: str, student_name: str):
    try:
        ast_student = get_ast_from_code_cell(ruta_archivo, nombre_funcion)
    except Exception as error:
        print("An error has occurred with the student", student_name)
        return error
    return ast_student


# Recibe la ruta del Notebook que contiene el código del alumno y el nombre de la función a evaluar. Lee el notebook y
# recorre todas las celdas, identifica las que son de código y las convierte a AST, y entonces mira si se encuentra la
# función que buscamos. Retorna la celda más larga, en el caso de que encuentre dos.
def get_ast_from_code_cell(ruta_archivo, nombre_funcion):
    list_ast = []
    index_ast = 0
    len_ast = 0

    with open(ruta_archivo, encoding="latin-1") as code:
        nb = nbformat.read(code, as_version=4)
        # Recorrer todas las celdas del notebook
        for celda in nb.cells:
            # Solo procesar las celdas del tipo código
            if celda.cell_type == "code":
                ast_student = ast.parse("".join(celda.source))
                for nodo in ast.walk(ast_student):
                    # Verificar si la celda contiene la función con el nombre que buscamos
                    if isinstance(nodo, ast.FunctionDef) and nodo.name == nombre_funcion:
                        list_ast.append(ast_student)

    # Si hemos encontrado dos celdas de código que contengan la función retornamos la más larga.
    if len(list_ast) > 1:
        for one_ast in range(len(list_ast)):
            if len_ast < len(ast.dump(list_ast[one_ast])):
                len_ast = len(ast.dump(list_ast[one_ast]))
                index_ast = one_ast
    return list_ast[index_ast]


# Función auxiliar que convierte un nodo AST en un nodo ZSS recorriendo los nodos del ZSS y paralelamente creado
# un árbol de Node() con el nombre y la lista de hijos, gracias a la recursión.
def convert_ast_to_zss_node(node, name, anterior=None):
    children = []

    if anterior is None:
        label = "None"
    else:
        label = type(node).__name__

    for child in ast.iter_child_nodes(node):
        new_child = convert_ast_to_zss_node(child, name, node)
        children.append(new_child)

    return Node(label, children)
