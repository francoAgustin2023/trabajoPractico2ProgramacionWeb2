#TableroMensajes

TableroMensajes es un proyecto de ejemplo desarrollado en Django, diseñado para permitir que dos usuarios (hardcodeados como Juan y María) puedan enviar, recibir y eliminar mensajes. 
El proyecto sigue el patrón de diseño Modelo-Vista-Plantilla (MVT), utilizando tanto vistas basadas en funciones como en clases, con una estructura modular y reutilización de plantillas.

##Instalación

###Requisitos previos
-  Tener instalado Python 3.x
- Tener pip para gestionar los paquetes de Python.
- Se recomienda usar un entorno virtual y tenerlo activado a la hora de ejecutar el proyecto.

##Pasos de instalación

###Clonar el repositorio: 

Clona este repositorio en tu máquina local.

**git clone <url del repositorio>**
**cd TableroMensajes**

###Crear un entorno virtual: 

Dentro de la carpeta del proyecto, crea y activa un entorno virtual.

**python -m venv env**

**source env/bin/activate  # En Windows: env\Scripts\activate**

###Instalar dependencias: 

Una vez activado el entorno virtual, instala las dependencias necesarias con el siguiente comando:

**pip install -r requirements.txt**

###Migrar la base de datos: 

Ejecuta las migraciones de Django para preparar la base de datos:

**python manage.py migrate**

##Ejecutar el servidor: 

Finalmente, ejecuta el servidor de desarrollo de Django.

**python manage.py runserver**

Accede a la aplicación en **http://127.0.0.1:8000/** (directorio raíz de la aplicación. Llevará a home).

En espe punto, ya se puede navegar tranquilamente desde los html sin ir igresando
manualmente mas URLs.

##Uso del proyecto

###Funcionalidades principales:

**Home:** Página principal que muestra enlaces para navegar por la aplicación.
**Crear Mensaje:** Permite a Juan o María crear un mensaje que puede ser enviado a uno de ellos.
**Ver Mensajes Recibidos:** Muestra los mensajes recibidos por Juan o María.
**Ver Mensajes Enviados: **Muestra los mensajes enviados por Juan o María.
**Eliminar Mensaje:** Permite eliminar un mensaje específico ingresando su ID (pk) en un formulario.

###Plantillas HTML:

**base.html: **Plantilla base que define la estructura principal del sitio.
**home.html: **Página de inicio que presenta los enlaces de navegación.
**crear_mensaje.html:** Página con un formulario para crear y enviar mensajes.
**mensajes_recibidos.html: **Página para ver los mensajes recibidos por un usuario.
**mensajes_enviados.html:** Página para ver los mensajes enviados por un usuario.
**eliminar_mensaje.html: **Página con un formulario para eliminar mensajes ingresando su ID.
Estructura del proyecto

El proyecto sigue la arquitectura MVT (Modelo-Vista-Plantilla). Las funcionalidades principales están divididas en:

**Vistas:** Las vistas basadas en clases y funciones manejan las solicitudes GET y POST, dirigiendo las interacciones con la base de datos y las plantillas.
**Modelos: **El modelo Mensaje es simple, con campos para el texto del mensaje, el remitente, el destinatario y la fecha de envío.
**Plantillas: **Las plantillas HTML están organizadas para reutilizar código mediante herencia (base.html).

##Notas adicionales

Este proyecto ha sido creado con fines educativos y está diseñado para ayudar a los estudiantes a aprender a manejar un proyecto Django con vistas basadas en clases y en funciones, uso de plantillas, y manejo básico de formularios y bases de datos. 
