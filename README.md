# Trabajo de Final de Grado (TFG) - UB 2023
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
- solution_directory_path = 'Datos/Soluciones/'
- student_evaluation = "Datos/Calificaciones_profesor_lab8.ods"
- num_col_name = 1
- num_col_surname = 0
- num_col_evaluation = 3

#### Commando para ejecución:
```python
  python main.py "subcadena_mes_llarga" "Datos/Entregas_alumnos" "Datos/Soluciones/" "Datos/Calificaciones_profesor_lab8.ods" 1 0 3
```

### El directorio que utilizamos como ejemplo sigue el siguiente formato:

#### · Directorio principal
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/199a4f66-9f64-40e5-97af-0cfba06f492f" alt="Descripción de la imagen" width="250">
  
#### · Directorio 'Datos/'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/4fb58e36-469b-41df-8f0e-f99a5e58dacb" alt="Descripción de la imagen" width="350">
  
#### · Directorio 'Datos/Entregas_alumnos/'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/1660cd89-315f-4930-8692-411c26c069b7" alt="Descripción de la imagen" width="500">

##### Las carpetas que contienen el Notebook Jupyter del alumnos DEBEN incluir el nombre del alumno, como en este ejemplo, para poder identificar de quien es cada código. Por privacidad se han canviado los nombres de las carpetas, pero deberian ser identificativos, y corresponder al nombre del Excel con sus notas manuales.
  
#### · Directorio 'Datos/Entregas_alumnos/APELLIDO1 APELLIDO2 NOMBRE(1)_669...'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/68a0e1bd-bf52-4e94-8ecb-ba6036096549" alt="Descripción de la imagen" width="300">
  
##### El nombre del Notebook del alumno no importa que nombre tenga.

#### · Directorio 'Datos/Soluciones/'
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/9df3bbf1-ef44-41e9-b324-a61ef19a98e7" alt="Descripción de la imagen" width="300">
  
##### No importa el nombre que tenga el notebook de las soluciones.

### El archivo 'Calificaciones_profesor_lab8.ods' que contiene las notas manuales sigue el siguiente formato:
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/80b5de7d-c516-4d3a-a2b6-5db9d3d95208" alt="Descripción de la imagen" width="500">

##### Por ese motivo añadimos los argumetnos num_col_name = 1, num_col_surname = 0, num_col_evaluation = 3 al ejecutar el programa. Recalco que el nombre identificativo del código del alumno se coge de su carpeta y que debe coincidir con el nombre + apellidos identificativos en esta tabla

## Resultado al ejecutar:
  
#### Se crea una carpeta en la carpeta principal que contiene todos los resultados.
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/dd3a4f72-8a0d-462c-b0f0-b2c7963cb7fe" alt="Descripción de la imagen" width="250"> <br>
  
#### Dentro de esa carpeta "Resultados" encontraremos lo siguiente:
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/29bce71d-6fe1-4655-80da-b7d12c781410" alt="Descripción de la imagen" width="300">

#### Ejemplo resultado ejecución: Diagrama_dispersión.png
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/229d29f0-ef02-43c2-85f5-856fe299ecb2" alt="Descripción de la imagen" width="400">

##### Ejemplo resultado ejecución: tabla_resultados.html
<image src="https://github.com/eperezba14/TFG_Estela_Perez_Bassedas/assets/72269905/c293e857-3082-4804-8577-242ea9ade7b0" alt="Descripción de la imagen" width="700">
