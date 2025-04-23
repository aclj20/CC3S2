
### Actividad: Pruebas BDD con behave en español

#### Instalación
Clona el repositorio y crea un entorno virtual llamado `act9`, luego actívalo.
![](img-act7/Pasted_image_20250420111619.png)  
![](img-act7/Pasted_image_20250420111734.png)
Instala las dependencias necesarias:
![](img-act7/Pasted_image_20250420113050.png)

#### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**
 
1. **Modifica** la función que maneja el tiempo de espera en `steps.py` 
![](img-act7/Pasted_image_20250420121523.png)

2. **Implementa** un escenario de prueba en Gherkin (`belly.feature`) agregue y pasaron
![](img-act7/Pasted_image_20250420122146.png)
3. **Considera** también crear pruebas unitarias con Pytest para la lógica de parsing (función que convierte el texto de tiempo en horas decimales).
![](img-act7/Pasted_image_20250420131320.png)
![](img-act7/Pasted_image_20250420132211.png)
![](img-act7/Pasted_image_20250420132148.png)
4. **En un entorno DevOps**:
   - Agrega la ejecución de `behave` y `pytest` en tu *pipeline* de CI/CD, de modo que al hacer push de los cambios se ejecuten automáticamente las pruebas.
   ![](img-act7/Pasted_image_20250420145930.png)
![](img-act7/Pasted_image_20250420153540.png)
#### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**

1. **Modifica** el sistema (la clase `Belly` y los steps en Behave) para que acepte entradas como `"0.5"`, `"2.75"`.
![](img-act7/Pasted_image_20250420175848.png)

2. **Implementa** un nuevo escenario en Gherkin donde se ingiera una cantidad fraccionaria y verifica el comportamiento.
![](Pasted_image_20250420175933.png)
3. **Valida** que el sistema lance una excepción o error si se ingresa una cantidad negativa de pepinos.
![](img-act7/Pasted_image_20250421101640.png)
![](img-act7/Pasted_image_20250421103606.png)
![](img-act7/Pasted_image_20250421101755.png)
4. **Pruebas unitarias**:  
   - Cubre el caso de pepinos fraccionarios en `test_belly.py`.
   - Cubre también el caso de pepinos negativos (se espera un error).
![](img-act7/Pasted_image_20250421103459.png)
![](img-act7/Pasted_image_20250421103534.png)

#### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**

1. **Modifica** el parsing de tiempo para que reconozca palabras clave en inglés, además de español (por ejemplo, `"two hours"`, `"thirty minutes"`).
![](img-act7/Pasted_image_20250422141537.png)

2. **Escribe** al menos dos escenarios de prueba en Gherkin que usen tiempos en inglés.
![](img-act7/Pasted_image_20250422142028.png)

3. **En un pipeline DevOps**, podrías:
   - Dividir los escenarios en distintos *tags* (`@spanish`, `@english`) y ejecutar cada conjunto en etapas diferentes, o en paralelo.
   ![](img-act7/Pasted_image_20250422144048.png)
	![](img-act7/Pasted image 20250422144743.png)


#### Ejercicio 4: **Manejo de tiempos aleatorios**

1. **Crea** una función que, dada una expresión como "entre 1 y 3 horas", devuelva un valor aleatorio entre 1 y 3 horas.
![](img-act7/Pasted_image_20250422152904.png)
![](img-act7/Pasted_image_20250422152925.png)


2. **Implementa** un escenario en Gherkin que verifique que, tras comer pepinos y esperar un tiempo aleatorio, el estómago puede gruñir.
	![](img-act7/Pasted_image_20250422153915.png)
3. **Imprime** (en consola o logs) el tiempo aleatorio elegido para que el resultado sea rastreable en tu pipeline.
	![](img-act7/Pasted_image_20250422154136.png)
	![](img-act7/Pasted_image_20250422155750.png)

4. **En un pipeline DevOps**:  
   - Considera utilizar un *seed* de aleatoriedad fijo para evitar *flakiness* (tests intermitentes).  
   ![](img-act7/Pasted_image_20250422160047.png)

#### Ejercicio 5: **Validación de cantidades no válidas**

1. **Añade** validaciones para evitar que el usuario ingrese < 0 pepinos o > 100 pepinos. y **modifica** la lógica para arrojar un error (excepción) si la cantidad no es válida.
![](img-act7/Pasted_image_20250422160603.png)

2. **Implementa** un escenario de prueba que verifique el comportamiento de error.
![](img-act7/Pasted_image_20250423034934.png)	![](img-act7/Pasted_image_20250422161239.png)
3. **En tu pipeline**, verifica que la excepción se maneje y el test falle de manera controlada si el sistema no lanza la excepción esperada.
	![[Pasted image 20250422161728.png]]

#### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**

1. **Implementa** un escenario en Gherkin para comer 1000 pepinos y esperar 10 horas.
	![](img-act7/Pasted_image_20250423034532.png)



#### Ejercicio 7: **Descripciones de tiempo complejas**

1. **En un pipeline**:  
   - Puedes analizar la cobertura de pruebas (coverage) para asegurarte de que la nueva lógica de parsing está completamente testeada.
![](img-act7/Pasted_image_20250422170634.png)


#### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**

1. **Escribe** un test unitario básico con Pytest que valide que si se han comido más de 10 pepinos y se espera 2 horas, el estómago gruñe.
![](img-act7/Pasted_image_20250422182858.png)
2. **Convierte** ese test unitario en un escenario Gherkin, con la misma lógica, pero más orientado al usuario.
![](img-act7/Pasted_image_20250422183958.png)

3. **En un pipeline DevOps**:
   - Ejecuta primero los tests unitarios (rápidos) y luego los tests de Behave (que pueden ser más lentos y de nivel de integración).
![](img-act7/Pasted_image_20250422184506.png)


