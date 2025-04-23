### Actividad: El patrón Arrange-Act-Assert

#####  Configuración de dependencias y ejecución

En el archivo `requirements.txt` asegúrate de incluir las dependencias necesarias:

![](img-act8/Pasted_image_20250422230624.png)


Para ejecutar las pruebas y generar el reporte de cobertura, puedes usar:

```bash
pytest --cov=src --cov-report=term-missing
```
![](img-act8/Pasted_image_20250422231028.png)

O bien, para generar un reporte HTML:

```bash
pytest --cov=src --cov-report=html
```
![](img-act8/Pasted_image_20250422231130.png)
![](img-act8/Pasted_image_20250422231359.png)
![](img-act8/Pasted_image_20250422231556.png)
![](img-act8/Pasted_image_20250422231618.png)

Y para el análisis estático con pylint:

![](img-act8/Pasted_image_20250422232932.png)


---
#### Ejercicios

##### Ejercicio 1: Método para vaciar el carrito

- Agrega el método `vaciar` en `src/carrito.py` que realice `self.items = []`.
![[Pasted image 20250422235140.png]]
- Crea pruebas en `tests/test_carrito.py` que agreguen varios productos, invoquen `vaciar()` y verifiquen que `obtener_items()` retorne una lista vacía y `calcular_total()` retorne 0.
![](img-act8/Pasted_image_20250422235117.png)

##### Ejercicio 2: Descuento por compra mínima

- Agrega un nuevo método, por ejemplo, `aplicar_descuento_condicional(porcentaje, minimo)` en la clase `Carrito` que primero verifique si `calcular_total() >= minimo`.  
![](img-act8/Pasted_image_20250422235730.png)

- Si se cumple la condición, aplica el descuento; de lo contrario, retorna el total sin descuento.
- Escribe pruebas para ambos escenarios (condición cumplida y no cumplida).
![](img-act8/Pasted_image_20250423000952.png)


##### Ejercicio 3: Manejo de stock en producto

- Modifica `Producto` en `src/carrito.py` añadiendo `self.stock = stock` en el constructor y actualiza la fábrica en `src/factories.py` para que genere un stock (por ejemplo, entre 1 y 100).
![](img-act8/Pasted_image_20250423003425.png)
- En `Carrito.agregar_producto`, antes de agregar o incrementar la cantidad, verifica que la suma de cantidades en el carrito no supere el `stock` del producto.
![](img-act8/Pasted_image_20250423003404.png)

- Escribe pruebas que verifiquen:
  - Se puede agregar un producto dentro del límite de stock.
  - Se lanza una excepción al intentar agregar más unidades de las disponibles.

![](img-act8/Pasted_image_20250423004848.png)

##### Ejercicio 4: Ordenar items del carrito

- Crea un método `obtener_items_ordenados(criterio: str)` donde `criterio` pueda ser `"precio"` o `"nombre"`.
- Utiliza la función `sorted()` con una función lambda para ordenar según el criterio.
![](img-act8/Pasted_image_20250423005537.png)


