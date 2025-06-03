### **Actividad: Gestión ágil de proyectos con GitHub Projects, configuración de Kanban Board y creación de historias de usuario**

#### Parte 1

En este ejercicio, configuramos un Kanban board usando GitHub Projects para el repositorio del curso.

Primero creamos un proyecto llamado devops
![Project](img/image-0.png)

Después de realizar cambios, tenemos 8 columnas en nuestro KanbanBoard
![alt text](img/image.png)
![alt text](img/image-1.png)
![alt text](img/image-2.png)
![alt text](img/image-3.png)

#### Parte 2

En este ejercicio, creamos una issue template en GitHub que nos ayudó a escribir historias de usuario bien formateadas en el Kanban board.

##### Crear una issue template en GitHub

En este ejercicio, creamos una issue template para las historias de usuario en GitHub.

![alt text](img/image-4.png)


####  Parte 3

En este ejercicio creamos historias de usuario basadas en los requisitos dados. 

- Deploy service to the cloud  
![alt text](img/image-5.png)
- Need the ability to remove a counter  
![alt text](img/image-6.png)
- Need the ability to update a counter to a new value  
![alt text](img/image-7.png)


#### Parte 4

En este ejercicio, seguimos los pasos para llevar a cabo una reunión de refinamiento del backlog. 

##### Hacer que las historias estén listas para el sprint

En esta parte, agregamos más detalles a las historias en el **Product Backlog** que c podrían entrar en el próximo sprint. 

Editamos los **Details** y **Assumptions** para que los desarrolladores sepan lo que sabemos. 

   - Deploy service to the cloud
   ![alt text](img/image-8.png)
   - Counters can be reset
   ![alt text](img/image-9.png)
   - Need ability to update a counter to a new value
   ![alt text](img/image-10.png)




##### Crear nuevas labels en GitHub

En este ejercicio, creamos una nueva label en GitHub llamada **technical debt** para marcar aquellas historias que no aportan valor visible al cliente pero deben completarse para continuar con el desarrollo.

![alt text](img/image-11.png)

##### Añadir labels a las historias

En este ejercicio, añadimos labels a las historias en el **Product Backlog** para hacerlas aún más listas para el sprint. 

![alt text](img/image-19.png)
![alt text](img/image-20.png)

### Ejercicios

##### Ejercicio 1: Crear un Epic y vincular historias de usuario

Creamos un nuevo Epic en el Kanban board llamado "Gestión de Contadores".
![alt text](img/image-13.png)

Vinculamos las historias de usuario existentes, como "Need a service that has a counter", "Must allow multiple counters", y "Counters can be reset" a este Epic y añadimos una nueva historia de usuario bajo este Epic que abarca una funcionalidad adicional 

![alt text](img/image-12.png)


##### Ejercicio 2: Uso avanzado de etiquetas (labels) para priorización y estado

Creamos nuevas etiquetas como **high priority**, **medium priority**, y **low priority**.

![alt text](img/image-14.png)

Luego, asignamos etiquetas a las historias de usuario que indiquen su prioridad
![alt text](img/image-16.png)
![alt text](img/image-17.png)
![alt text](img/image-15.png)

##### Ejercicio 3: Automatización de Kanban board con GitHub Actions

Creamos un archivo de configuración de GitHub Actions en la carpeta `.github/workflows` que defina estas reglas de automatización.

Las historias de usuario se mueven automáticamente en el Kanban board según las reglas definidas.
![alt text](img/image-18.png)


##### Ejercicio 4: Seguimiento de tiempo y esfuerzo usando GitHub Projects

Usamos el seguimiento de tiempo y esfuerzo para las historias de usuario en GitHub Projects.

Añadimos un campo personalizado Time Todo en el Kanban board para registrar el esfuerzo estimado de cada historia de usuario (en horas).
![alt text](img/image-21.png)




