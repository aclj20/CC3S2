### Actividad 11: Escribir aserciones en pruebas con pytest

**Paso 1: Instalación de pytest y pytest-cov**
En esta actividad se practica el uso de `pytest` para ejecutar pruebas unitarias, identificar fallos mediante aserciones y generar informes de cobertura con `pytest-cov`.

Primero, instalamos `pytest` y `pytest-cov` ejecutando en la terminal:
![](img-11/Pasted_image_20250506105302.png)


**Paso 2: Archivos de prueba**

La estructura consta de dos archivos para esta actividad: `stack.py` y `test_stack.py`.
![](img-11/Pasted_image_20250506112503.png)

- `stack.py`: Contiene la implementación de una pila (stack) que queremos probar.
- `test_stack.py`: Contiene el esqueleto de las pruebas para los métodos `push()`, `pop()`, `peek()`, y `is_empty()`.

Antes de escribir los casos de prueba, revisemos los métodos de la clase `Stack`:

![](img-11/Pasted_image_20250506112626.png)

Descripción de funciones:

- `push()`: Añade un elemento a la parte superior de la pila.
- `pop()`: Elimina y devuelve el elemento en la parte superior de la pila.
- `peek()`: Devuelve el valor del elemento en la parte superior de la pila sin eliminarlo.
- `is_empty()`: Devuelve True si la pila está vacía y False si no lo está.



Se verificó la ejecución de las pruebas usando `pytest -v`, confirmando que todos los casos (`is_empty`, `peek`, `pop` y `push`) pasaron exitosamente.
![](img-11/Pasted_image_20250506113322.png)

Se verificó usando `pytest -x`, que permite detener la ejecución al primer fallo, útil para identificar rápidamente errores sin ejecutar todos los tests.

![](img-11/Pasted_image_20250506113343.png)


Por defecto, pytest ejecuta las pruebas en el orden en que están definidas en los archivos. Para usar un orden aleatorio, se puede emplear el plugin `pytest-randomly`, útil para detectar dependencias entre pruebas.

Instalamos el plugin con `pip install pytest-random-order`
![](img-11/Pasted_image_20250506113503.png)

Luego ejecutamos las pruebas con `pytest --random-order` para validarlas en un orden aleatorio, verificando así su independencia.
![](img-11/Pasted_image_20250506113525.png)


**Paso 3: Escribiendo aserciones para el método `is_empty()`**

El método `test_is_empty` verifica que una pila nueva esté vacía y que deje de estarlo después de insertar un elemento.
![](img-11/Pasted_image_20250506114537.png)


El método `test_pop` comprueba que los elementos se extraigan en orden correcto (LIFO) y que la pila quede vacía después de eliminar todos los elementos.
![](img-11/Pasted_image_20250506114554.png)


**Paso 4: Ejecuta pytest para verificar `is_empty()`**

Se ejecutó `pytest -v` para verificar que la prueba del método `is_empty()` pase correctamente, y como muestra la salida, todas las pruebas fueron exitosas.
![](img-11/Pasted_image_20250506114644.png)


**Paso 5: Escribiendo aserciones para el método `peek()`**

El test `test_peek()` verifica que `peek()` devuelva correctamente el último elemento agregado sin eliminarlo de la pila.  
![](img-11/Pasted_image_20250506114837.png)

El test `test_peek_with_setup()` confirma lo mismo, pero usando una pila preconfigurada con `setUp`.
![](img-11/Pasted_image_20250506120651.png)


Se ejecutó `pytest -v` para verificar que la prueba del método `peek()` pase correctamente, y como muestra la salida, todas las pruebas fueron exitosas.
![](img-11/Pasted_image_20250506120606.png)


**Paso 6: Escribiendo aserciones para el `método pop()`**

El test `test_pop()` verifica que el método `pop()` elimine y devuelva correctamente el último elemento agregado y que el nuevo tope de la pila sea el siguiente valor.

![](img-11/Pasted_image_20250506121305.png)


El test `test_pop_with_setup()` usa `self.stack` y realiza una prueba más completa: agrega dos elementos, comprueba que `pop()` devuelve el último, que `peek()` muestra el anterior, elimina ese también, y finalmente valida que la pila quede vacía.

![](img-11/Pasted_image_20250506121315.png)


Se ejecutó `pytest -v` para verificar que la prueba del método `pop()` pase correctamente, y como muestra la salida, todas las pruebas fueron exitosas.
![](img-11/Pasted_image_20250506122224.png)


**Paso 7: Escribiendo aserciones para el `método push()`**

El test `test_push()` comprueba que al insertar elementos con `push()`, el último añadido sea el que se encuentre en la parte superior de la pila. 
![](img-11/Pasted_image_20250506122135.png)

El test `test_push_with_setup()` valida lo mismo pero usando `self.stack`, asegurando que `peek()` siempre muestre el último valor insertado.
`
![](img-11/Pasted_image_20250506122035.png)


**Paso 8: Ejecuta pytest para verificar todas las pruebas**
Se ejecutó `pytest -v` para verificar que la prueba del método `push()` pase correctamente, y como muestra la salida, todas las pruebas fueron exitosas.
![](img-11/Pasted_image_20250506122154.png)


**Paso 9: Agregando cobertura de pruebas con pytest-cov**

Se ejecutó el comando `pytest --cov=stack --cov-report term-missing` para generar un informe de cobertura, el cual muestra el porcentaje de líneas de código de `stack.py` que están siendo cubiertas por las pruebas, así como las líneas que aún no han sido probadas.
![](img-11/Pasted_image_20250506122531.png)


**setup.cfg**
Este es un archivo de configuración para pytest y coverage, que personaliza cómo se ejecutan las pruebas y cómo se recopila el informe de cobertura de código. 
![](img-11/Pasted_image_20250506123444.png)


`[tool:pytest]` Esto indica que las configuraciones que siguen son para la herramienta pytest, el marco de pruebas en Python.
![](img-11/Pasted_image_20250506123244.png)


- `-v`: Muestra las pruebas con más detalle durante la ejecución.
- `--tb=short`: Acorta el rastro de errores para hacerlo más legible.
- `--cov=stack`: Calcula la cobertura del archivo o módulo `stack.py`.
- `--cov-report=term-missing`: Muestra en terminal las líneas de código no cubiertas por las pruebas.

`[coverage:run]` Este bloque contiene configuraciones específicas para el comando coverage run, que ejecuta las pruebas y recopila datos de cobertura.
![](img-11/Pasted%20image%2020250506123302.png)


- `branch = True`: Activa la cobertura de ramas, evaluando tanto la condición verdadera como falsa en estructuras como `if`.
- `omit = */tests/*`: Excluye todos los archivos ubicados dentro de carpetas llamadas `tests` del informe de cobertura.
- `omit = */test_*`: Excluye archivos cuyo nombre comienza con `test_`, como los de pruebas unitarias, para enfocarse solo en el código funcional.

`[coverage:report]`Este bloque define cómo se debe generar el informe de cobertura de código después de ejecutar las pruebas.
![](img-11/Pasted%20image%2020250506123313.png)

 - `show_missing = True`: Muestra en el informe las líneas de código que no fueron cubiertas por las pruebas, facilitando la identificación de partes no testeadas.
