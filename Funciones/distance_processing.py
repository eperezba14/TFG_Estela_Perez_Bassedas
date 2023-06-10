from zss import simple_distance
from Funciones.ast_processing import convert_ast_to_zss_node


# Convierte el AST del estudiante y el de la solución en un árbol ZSS, a más cuenta el número de nodos del árbol ZSS
# tanto del estudiante como de la solución y retorna la distancia entre estos.
def calculate_distance(ast_student, ast_solution):
    zss_node_student = convert_ast_to_zss_node(ast_student, "ast_solution", 0)
    counter_student = count_nodes(zss_node_student)
    zss_node_solution = convert_ast_to_zss_node(ast_solution, "ast_student", 0)
    counter_solution = count_nodes(zss_node_solution)
    return simple_distance(zss_node_solution, zss_node_student), (counter_student,counter_solution)


# Calcula el número total de nodos en ambos árboles ZSS, normaliza la distancia con una disivión y finalmente retorna
# la puntuación automática obtenida.
def normalized_tree_edit_distance(counter_student, counter_solution, distance):

    total_nodes = counter_student + counter_solution
    normalized_dist = distance / total_nodes
    return round((1-normalized_dist)*100, 2)


# Inicializa el contador en 1 para contar el nodo actual y recorre los hijos del nodo actual y suma al contador los
# nodos de cada hijo.
def count_nodes(zss_node):

    count = 1
    for child in zss_node.children:
        count += count_nodes(child)
    return count
