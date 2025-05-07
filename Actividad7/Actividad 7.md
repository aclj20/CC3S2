
### Actividad: Pruebas BDD con behave en español

#### Instalación

Primero, cloné el repositorio en mi máquina local. Luego, procedí a crear un entorno virtual con el nombre `act9` y luego lo active.
![](img-act7/Pasted_image_20250420111619.png)  
![](img-act7/Pasted_image_20250420111734.png)

También, instale las dependencias necesarias:
![](img-act7/Pasted_image_20250420113050.png)

#### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**
 
Modifiqué la función para interpretar descripciones de tiempo como "media hora" o "2 horas 30 minutos", utilizando expresiones regulares y convirtiendo palabras a números. Si la descripción no es válida, lanza un error.
![](img-act7/Pasted_image_20250420121523.png)

He implementado y ejecutado escenarios de prueba en Gherkin dentro del archivo `belly.feature`. Probé descripciones de tiempo de espera tanto en segundos como en formatos más complejos, todos los escenarios pasaron correctamente.
![](img-act7/Pasted_image_20250420122146.png)

He creado pruebas unitarias con Pytest para la función de parsing, que convierte el texto de tiempo en horas decimales.
![](img-act7/Pasted_image_20250420131320.png)
Utilicé la marca `@pytest.mark.parametrize` para probar varios casos. Las pruebas verifican que el resultado de la función se ajuste a los valores esperados, considerando posibles variaciones en el formato de entrada, como minutos y segundos.

![](img-act7/Pasted_image_20250420132211.png)

He ejecutado las pruebas unitarias con Pytest y todas han pasado correctamente.
![](img-act7/Pasted_image_20250420132148.png)

He agregado la ejecución de las pruebas con `pytest` y `behave` en la pipeline de CI/CD utilizando un archivo `tests.yml`. Este archivo se encuentra en el directorio `.github/workflows` y está configurado para ejecutar las pruebas automáticamente al hacer un push en la rama principal (`main`).
   
   ![](img-act7/Pasted_image_20250420145930.png)

El workflow de CI/CD se ha ejecutado correctamente tras realizar un push en la rama `main`. El pipeline configurado en el archivo `tests.yml` ejecutó las pruebas de forma exitosa.
![](img-act7/Pasted_image_20250420153540.png)
#### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**

He modificado la clase `Belly` y los steps en Behave, para que acepte entradas como "0.5" o "2.75" al registrar la cantidad de pepinos que se han comido.

Convierto la entrada a un número flotante usando `float()` y, si falla, lanzo un `ValueError`.
![](img-act7/Pasted_image_20250420175848.png)

He implementado un nuevo escenario en Gherkin para verificar el comportamiento cuando se ingiere una cantidad fraccionaria de pepinos.
![](img-act7/Pasted_image_20250420175933.png)

He validado que el sistema lance una excepción si se ingresa una cantidad negativa de pepinos.

Agregué una validación para asegurarse de que no se pueda ingresar una cantidad negativa de pepinos. Si se intenta, se lanza un `ValueError` con un mensaje adecuado.

![](img-act7/Pasted_image_20250421101640.png)

En este escenario, intenté ingresar una cantidad negativa de pepinos (-3), lo que generó correctamente una excepción con el mensaje "No se puede comer una cantidad negativa de pepinos".

![](img-act7/Pasted_image_20250421103606.png)

Esto fue confirmado por el error mostrado en el traceback, donde el `ValueError` fue lanzado como se esperaba
![](img-act7/Pasted_image_20250421101755.png)

Usé `pytest.mark.parametrize` para probar varios casos, incluidos valores negativos como "-1" y "-0.5", y aseguré que lanzaran un `ValueError` con el mensaje esperado "No se puede comer una cantidad negativa de pepinos". Además, también probé casos con pepinos fraccionarios como "2.5", "0.5", y "3.0", y verifiqué que los resultados se ajusten correctamente a los valores esperados.
![](img-act7/Pasted_image_20250421103459.png)
He ejecutado las pruebas unitarias con `pytest` y todas las pruebas pasaron correctamente.
![](img-act7/Pasted_image_20250421103534.png)

#### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**

He modificado el parsing de tiempo para que reconozca tanto palabras clave en español como en inglés. Añadí soporte para frases como "two hours", "thirty minutes" en inglés. También reemplazé el "and" en las descripciones en inglés por un espacio en blanco y manejé el caso especial de "half hour" para que se interprete correctamente.

![](img-act7/Pasted_image_20250422141537.png)

He escrito dos escenarios de prueba en Gherkin que utilizan tiempos en inglés, como se solicitó.
![](img-act7/Pasted_image_20250422142028.png)

He dividido los escenarios en dos grupos con los tags `@spanish` y `@english`, lo que permite ejecutarlos en etapas diferentes en un pipeline de DevOps.

Los escenarios con el tag `@spanish` verifican el comportamiento con descripciones de tiempo en español
![](img-act7/Pasted_image_20250422144048.png)

Mientras que los de `@english` verifican las descripciones en inglés.

![](img-act7/Pasted_image_20250422144743.png)


#### Ejercicio 4: **Manejo de tiempos aleatorios**

He creado una función que, al recibir una descripción como "entre 1 y 3 horas", extrae los límites inferior y superior de la descripción de tiempo y devuelve un número aleatorio dentro de ese rango usando `random.uniform()`.
![](img-act7/Pasted_image_20250422152904.png)
![](img-act7/Pasted_image_20250422152925.png)

He implementado un escenario en Gherkin para verificar que, después de comer pepinos y esperar un tiempo aleatorio (entre 2 y 4 horas), el estómago pueda gruñir.

![](img-act7/Pasted_image_20250422153915.png)

He modificado el código para que, además de generar el tiempo aleatorio, también lo imprima en la consola
![](img-act7/Pasted_image_20250422154136.png)

En este escenario, se generó un tiempo aleatorio de 1.34 horas pero la prueba falló porque se esperaba que el estómago gruñera después de esperar entre 1 y 2 horas. Sin embargo, el tiempo generado fue más cercano a 1 hora, lo que no cumplió con la condición de que el estómago debería gruñir después de ese tiempo.
![](img-act7/Pasted_image_20250422155750.png)

He utilizado un `seed` fijo (`random.seed(20)`) para asegurar resultados consistentes en las pruebas y evitar problemas de "flakiness" en el pipeline de DevOps.

![](img-act7/Pasted_image_20250422160047.png)

#### Ejercicio 5: **Validación de cantidades no válidas**

He añadido validaciones para asegurar que la cantidad de pepinos ingresada esté entre 0 y 100. Si el usuario ingresa una cantidad negativa o mayor a 100, se lanza un `ValueError` . Además, la función también maneja el caso donde no se puede convertir la entrada a un número flotante, lanzando un error en caso de que el formato de la cantidad sea inválido.

![](img-act7/Pasted_image_20250422160603.png)

He implementado dos escenarios en Gherkin para verificar que el sistema lance errores cuando se ingresa una cantidad negativa de pepinos o una cantidad mayor a 100. 

![](img-act7/Pasted_image_20250423034934.png)	

He añadido steps para verificar que las excepciones se manejen correctamente. Si no se lanza la excepción esperada, el test falla, asegurando un manejo adecuado de errores en el sistema.
![](img-act7/Pasted%20image%2020250422161728.png)

#### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**

He implementado un escenario en Gherkin para verificar el comportamiento del sistema al comer una gran cantidad de pepinos (1000) y esperar 10 horas.
![](img-act7/Pasted_image_20250423034532.png)

#### Ejercicio 7: **Descripciones de tiempo complejas**

He analizado la cobertura de pruebas utilizando la herramienta `coverage` en el pipeline. Esto me permitió asegurarme de que la lógica del parsing esté completamente testeada. El análisis mostró que, aunque se cubrió una gran parte del código, algunas áreas no estaban completamente probadas. Por ejemplo, el archivo `src/belly.py` tiene una cobertura del 0%, lo que indica que no se han ejecutado pruebas sobre ese código. La cobertura total fue del 58%, por lo que es recomendable mejorar la cobertura para asegurar que toda la lógica esté adecuadamente validada.

![](img-act7/Pasted_image_20250422170634.png)


#### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**

He creado un test con `pytest` que valida que, si se comen más de 10 pepinos y se espera 2 horas, el estómago gruñe, verificando que el método `esta_gruñendo()` devuelva `True`.

![](img-act7/Pasted_image_20250422182858.png)

He convertido el test unitario en un escenario Gherkin, donde tras comer 15 pepinos y esperar 2 horas, el estómago debería gruñir, de manera más orientada al usuario.

![](img-act7/Pasted_image_20250422183958.png)

En el pipeline de DevOps, ejecuto primero los tests unitarios con `pytest`, que son rápidos, y luego los tests de Behave, que son más lentos y de nivel de integración, separados por los tags `@spanish` y `@english`.

![](img-act7/Pasted_image_20250422184506.png)

#### Ejercicio 9: **Identificación de criterios de aceptación para historias de usuario**

He identificado los criterios de aceptación de la historia de usuario y los reflejé en dos escenarios Gherkin. El primero verifica que comer suficientes pepinos y esperar el tiempo adecuado hace que el estómago gruñe, mientras que el segundo valida lo contrario.

![](img-act7/Pasted%20image%2020250506232456.png)

He implementado los pasos en Behave para gestionar los escenarios, validando la cantidad de pepinos, procesando el tiempo esperado y verificando si el estómago gruñe o no, utilizando aserciones para comprobar el comportamiento esperado.
![](img-act7/Pasted%20image%2020250506232642.png)


#### Ejercicio 10: **Escribir pruebas unitarias antes de escenarios BDD**

He escrito un test unitario para la función `pepinos_ingestados()`, que retorna el total de pepinos ingeridos. 

![](img-act7/Pasted%20image%2020250507000249.png)

El test asegura que después de comer 15 pepinos, el valor retornado sea 15, siguiendo la secuencia TDD antes de implementar los escenarios en BDD.

![](img-act7/Pasted%20image%2020250507000332.png)

He creado un escenario en Gherkin donde, tras comer 15 pepinos, el usuario consulta y ve que ha comido 15 pepinos.
![](img-act7/Pasted%20image%2020250506234143.png)

He implementado los pasos en Behave para verificar que, al consultar la cantidad de pepinos ingeridos, el resultado coincida con el valor esperado.

![](img-act7/Pasted%20image%2020250506235406.png)

![](img-act7/Pasted%20image%2020250507000511.png)

El escenario en Gherkin se ejecutó correctamente.
![](img-act7/Pasted%20image%2020250507000943.png)

#### Ejercicio 11: **Refactorización guiada por TDD y BDD**

He refactorizado el código existente siguiendo la metodología TDD y BDD. Primero, elegí la funcionalidad `esta_gruñendo()` y luego aseguré que existan pruebas unitarias parametrizadas para cubrir casos clave. Utilicé `pytest.mark.parametrize` para probar diferentes combinaciones de pepinos, horas y si el estómago debería gruñir o no.

![](img-act7/Pasted%20image%2020250507001826.png)


He refactorizado el código para mejorar la eficiencia y reducir la duplicación. Ahora, en lugar de repetir la misma lógica en el método `esta_gruñendo()`, he creado un método auxiliar llamado `gruñir_condiciones()` que devuelve la condición para que el estómago gruña.

![](img-act7/Pasted%20image%2020250507002437.png)

He validado que todas las pruebas unitarias y los escenarios BDD siguen pasando correctamente sin cambios.

![](img-act7/Pasted%20image%2020250507002425.png)

![](img-act7/Pasted%20image%2020250507002507.png)

He activado la medición de cobertura en el pipeline utilizando `pytest` con las opciones `--cov` para indicar la carpeta de código fuente y `--cov-report` para generar un reporte en formato terminal y HTML.

![](img-act7/Pasted%20image%2020250507002719.png)

#### Ejercicio 12: **Ciclo completo de TDD a BDD – Añadir nueva funcionalidad**

He desarrollado una nueva funcionalidad desde cero utilizando TDD y BDD. En este caso, la funcionalidad predice si el estómago gruñirá dado un número de pepinos y un tiempo de espera.

![](img-act7/Pasted%20image%2020250507002913.png)

He convertido el test en una historia de usuario y escrito el escenario BDD correspondiente.

"**Como** usuario que ha comido una cierta cantidad de pepinos,  
**quiero** saber si mi estómago va a gruñir después de esperar un tiempo determinado,  
**para** poder anticiparme y tomar una acción ."

![](img-act7/Pasted%20image%2020250507004348.png)

He implementado la nueva funcionalidad y verificado que tanto la prueba unitaria como el escenario Gherkin pasen correctamente.
![](img-act7/Pasted%20image%2020250507004407.png)
![[Pasted image 20250507004426.png]]

#### Ejercicio 13: **Añadir criterios de aceptación claros**

He definido una nueva historia de usuario 

"**Como** usuario,  
**quiero** saber cuántos pepinos más puedo comer antes de que mi estómago gruña,  
**para** poder evitar molestias."

Identifique 3 criterios de aceptación
- Si he comido menos de 10 pepinos, el sistema me dirá cuántos más puedo comer antes de que gruñiría.
- Si ya he comido más de 10 pepinos, el sistema dirá que no puedo comer más.
- El sistema debe considerar que necesito al menos 1.5 horas de espera para que el estómago gruña.

Convertí esos criterios en escenarios BDD.
![](img-act7/Pasted%20image%2020250507010531.png)

 Luego, implemente los steps correspondientes

![](img-act7/Pasted%20image%2020250507010604.png)

**En un pipeline**, agrupé los escenarios bajo un mismo *tag* (`@criterio_nuevo`) para ejecutarlos juntos.

![](img-act7/Pasted%20image%2020250507010900.png)

#### Ejercicio 14: **Integración con Mocking, Stubs y Fakes (para DevOps)**


**Cree** un archivo `clock.py` con una función `get_current_time()`.

![](img-act7/Pasted%20image%2020250507011716.png)

**Modifiqué** `Belly` para aceptar un `clock_service` opcional que se inyecta.
![](img-act7/Pasted%20image%2020250507011746.png)

Cree un test unitario con Pytest que use `unittest.mock` para simular el paso del tiempo.

![](img-act7/Pasted%20image%2020250507011832.png)
 
**En Behave**, usé `environment.py` para inyectar un mock o stub del reloj en el `before_scenario`.

![](img-act7/Pasted%20image%2020250507012149.png)

Todos los escenarios y pasos en los tests se ejecutaron correctamente. La salida muestra que 20 escenarios pasaron sin errores, con 60 pasos completados exitosamente.

![](img-act7/Pasted%20image%2020250507012409.png)



---

