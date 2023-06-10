# Trabajo de final de grado - Universidad de Barcelona 2023
#### Autora: Estela Pérez Bassedas
#### Título: Evaluación automática de programas en Python a partir de árboles de sintaxis abstracta

## Pasos para ejecutar:
#### Librerias necesarias:
- ast
- nbformat
- zss (Node/simple_distance)
- csv
- os
- ezodf
- matplotlib.pyplot
- pandas
- unidecode

#### Explicación de cada argumento:
- **function_name** -> Nombre de la función a evaluar.
- **submissions_path** -> Path del directorio que contiene las entregas de los alumnos.
- **solution_path** -> Path del archivo con la solución de referencia.
- **student_evaluation** -> Path del archivo csv que contiene las evaluaciones manuales de los alumnos.
- **num_col_name** -> Número de la columna que corresponde al nombre dentro del archivo excel que contiene la evaluación manual del estudiante.
- **num_col_surname** -> Número de la columna que corresponde al apellido dentro del archivo excel que contiene la evaluación manual del estudiante.
- **num_col_evaluation** -> Número de la columna que corresponde a la nota dentro del archivo excel que contiene la evalución manual del estudiante.

#### Commando para ejecución:
```python
  python main.py function_name submissions_path solution_path student_evaluation num_col_name num_col_surname num_col_evaluation
```
## Ejemplo concreto con el que se ha estado trabajando
#### Ejemplo de argumentos para ejecutar este código en Python:
- function_name = 'subcadena_mes_llarga'
- submissions_path = 'Datos/Entregas_alumnos'
- solution_path = 'Datos/Solución_profesor.ipynb'
- student_evaluation = "Datos/Calificaciones_profesor_lab8.ods"
- num_col_name = 1
- num_col_surname = 0
- num_col_evaluation = 3

#### Commando para ejecución:
```python
  python main.py "subcadena_mes_llarga" "Datos/Entregas_alumnos" "Datos/Solución_profesor.ipynb" "Datos/Calificaciones_profesor_lab8.ods" 1 0 3
```

### El directorio que utilizamos como ejemplo sigue el siguiente formato:

#### · Directorio principal
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/67c20e5b-b697-4946-b058-4688e51d656f" alt="Descripción de la imagen" width="150">
  
#### · Directorio 'Datos/'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/762adfdd-7b84-4c03-b999-8c2639deca3d" alt="Descripción de la imagen" width="300">
  
#### · Directorio 'Datos/Entregas_alumnos/'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/606499fa-7614-4e7a-8aba-6027e3b4eac8" alt="Descripción de la imagen" width="400">

##### Las carpetas que contienen el notebook jupyter del alumnos DEBEN incluir el nombre del alumno, como en este ejemplo, para poder identificar de quien es cada código.
  
#### · Directorio 'Datos/Entregas_alumnos/AMARO VELASCO EMMA_6698714...'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/acb4be20-5700-4566-ae9f-e5bfee7fd2c6" alt="Descripción de la imagen" width="300">

##### El nombre del notebook del alumno no importa que nombre tenga.

### El archivo 'Calificaciones_profesor_lab8.ods' que contiene las notas manuales sigue el siguiente formato:
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/3d9169f6-d5a3-4c07-bdcb-55d320379aa7" alt="Descripción de la imagen" width="500">

##### Por ese motivo añadimos los argumetnos num_col_name = 1, num_col_surname = 0, num_col_evaluation = 3 al llamar a la función.

