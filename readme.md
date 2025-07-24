# Instrucciones de Uso

## Estructura del Proyecto

```
proyecto_ADA/
│
├── core/
│   ├── array_sol_classes.py
│   ├── auxiliar_functions.py
│   ├── generator.py
│   ├── tree_sol_classes.py
│
├── tests/
│   ├── Test1.txt
│   ├── Test2.txt
│   ├── ... (más archivos de prueba)   
│
├── main.py
```

## Ejecución

1. Configurar en `main.py` los parámetros de ejecución

```python
  inputPath = "tests/Test1.txt" # Path al test a ejecutar (test singular)
  # 0 para ejecutar todos los tests en tests\, 1 ejecutar solo el test en inputPath
  mode = 0 
  # 0 para solución de Arrays, 1 para BSTs
  solution = 1 
```

2. Abrir una terminal en la raíz del proyecto.
3. Ejecutar el archivo principal:

```
python main.py
```

## Creación de Tests

1. Configurar en `core\generator.py` los parámetros de ejecución

```python
K = 2 # Número de temas
M = 2 # Número de preguntas por tema
Nmin = 3 # Mínimo número de encuestados por pregunta
Nmax = 5 # Máximo número de encuestados por pregunta
mode = "random" # Modo de generación
path = "tests/Test4.txt" # Ruta donde guardar el output

"""
"random" significa que cada pregunta tendrá P encuestados donde P es un número natural entre Nmin y Nmax.
"min" significa que cada pregunta tendrá Nmin encuestados.
"max" significa que cada pregunta tendrá Nmax encuestados.
"""
```

2. Abrir una terminal en la raíz del proyecto.
3. Ejecutar el archivo:

```
python core\generator.py
```



