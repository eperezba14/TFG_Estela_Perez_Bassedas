from zss import simple_distance
from Funciones.ast_processing import convert_ast_to_zss_node


# Convierte el AST del estudiante y el de la solución en un árbol ZSS, a más cuenta el número de nodos del árbol ZSS
# tanto del estudiante como de la solución y retorna la distancia entre estos.
def calculate_distance(ast_student, ast_solution):
    zss_node_student = convert_ast_to_zss_node(ast_student, "ast_solution")
    counter_student = count_nodes(zss_node_student)
    zss_node_solution = convert_ast_to_zss_node(ast_solution, "ast_student")
    counter_solution = count_nodes(zss_node_solution)
    simple_d, operations = simple_distance(zss_node_student, zss_node_solution, return_operations=True)
    dict_operations = num_of_operation(operations)
    print(dict_operations)
    return simple_d, (counter_student, counter_solution), dict_operations


# Calcula el número total de nodos en ambos árboles ZSS, normaliza la distancia con una disivión y finalmente retorna
# la puntuación automática obtenida.
def normalized_tree_edit_distance(counter_student, counter_solution, distance):
    total_nodes = counter_student + counter_solution
    normalized_dist = distance / total_nodes
    return round((1 - normalized_dist) * 100, 2)


# Inicializa el contador en 1 para contar el nodo actual y recorre los hijos del nodo actual y suma al contador los
# nodos de cada hijo.
def count_nodes(zss_node):
    count = 1
    for child in zss_node.children:
        count += count_nodes(child)
    return count


# Como argumento le llega una lista que recorremos y vamos aumentando el contador de la operación realizada dentro
# de un diccionario. Retornamos la información de ese diccionario escrita en una cadena.
def num_of_operation(operations):
    str_operations = ""
    num_operation = {"Eliminar": 0, "Insertar": 0, "Etiquetar": 0, "Iguales": 0}

    for operation in operations:
        if operation.type == operation.remove:
            num_operation["Eliminar"] += 1
        elif operation.type == operation.insert:
            num_operation["Insertar"] += 1
        elif operation.type == operation.update:
            num_operation["Etiquetar"] += 1
        elif operation.type == operation.match:
            num_operation["Iguales"] += 1

    # Recorremos el diccionario y escribimos en una cadena la clave y el valor correspondiente.
    for clave, valor in num_operation.items():
        str_operations += clave + ": " + valor.__str__() + " / "
    str_operations = str_operations[:-2]

    return str_operations
