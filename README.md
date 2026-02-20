# Proyecto Django: Gestión de Rutas de Autobús

## Descripción
El proyecto consiste en en tres modelos (Autobús, Zona y Elección) que se suman al modelo base User para presentar a cada usuario nuevo que se registre distintas opciones de autobuses 
para que las pueda añadir en un CRUD sólo accesible desde su sesión (fuera del entorno admin). A continuación se presentarán algunas capturas del proceso de registro y creación de elecciones
propias, así como algunos fragmentos de código de los modelos más complejos (Autobús y Elección). 

## Vista de login:
Pantalla a la que se redirige a cualquier usuario que carezca de token de sesión, si un usuario ya está registrado accede indicando su nombre de usuario y contraseña, si carece de cuenta
puede crear una registrándose.

![Pantalla de login](imagenes/login.png)

## Vista de sign up:
Pantalla a la que se accede en caso de querer crear una nueva cuenta de usuario. Se pedirá nombre, contraseña y confirmación de esta. La contraseña debe contener 8 caracteres mínimo e intercalar
números y letras

![Pantalla de sign up](imagenes/registro.png)

## Vista de elecciones:
Esta es la primera vista a la que se accede tras haberte identificado o registrado. En caso de no tener ninguna elección todavía la tabla muestra un texto indicando la falta de datos de elección.
Desde esta misma vista se puede acceder a las secciones de zonas y autobuses para ver las opciones disponibles. Esto se hace mediante una barra de navegación heredada del archivo Templates/base.html mediante
templates de django.

![Pantalla de elecciones](imagenes/elecciones.png)

## Vista de creación de elecciones:
En esta vista aparece un menú desplegable que accede a todos los autobuses disponibles para que al pulsar sobre uno y sobre el botón guardar se añada a la lista personal de elecciones

![Pantalla de elecciones](imagenes/crearEleccion.png)
![Pantalla de elecciones 2](imagenes/crearEleccion2.png)

## Panel de administración:
Este es el panel de administración que django trae por defecto, desde este se pueden gestonar aquellos apartados a los que un usuario cualquiera no puede acceder, el registro de zonas y autobuses.

![Panel admin](imagenes/panel.png)

## Código de los modelos Autobús y Elección:
### Modelo Autobús:
Este modelo presenta una relación 1:n con respecto al modelo Zona (foreign key) mediante el cual una zona puede tener varios autobuses pero un autobús solo pertenece a una zona. En este fragmento de
código cabe destacar el uso de on_delete=models.CASCADE y el de la clase meta para especificar el nombre que aparece en el administrador en plural. Esto lo hice porque por defecto, al hacer una palabra
plural, añade una s como protocolo general. Lo cual hacía que el plural de autobús apareciera como autobuss. 

![Modelo Autobús](imagenes/autobus.png)

### Modelo Elección:
Modelo que hace de puente entre Autobús y Zona. Como este modelo es el que va atado a cada usuario concreto que registre elecciones, es el único modelo en que ha sido necesaro importar
get_user_model para detectar qué usuario está creando registros de este y que se muestre así una tabla personalizada según el usuario. Otro aspecto a destacar de este fragmento de código 
es la presencia de la regla de negocio que impide a un usuario elegir dos veces el mismo autobús. Esto se consigue mediante models.UniqueConstraint que crea una restricción de unicidad sobre
los campos usuario y autobús.

![Modelo Elección](imagenes/eleccion.png)






