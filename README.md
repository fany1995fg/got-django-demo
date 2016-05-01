# Taller de Django

Comandos utilizados en el taller
================================
Requisitos
----------
*Instalar python3*  
[Descargar python3](https://www.python.org/downloads/windows/)

Trabajando con pip y virtualenv en windows
------------------------------------------
*Creando un entorno virtual*

    C:\Python34\python -m venv myvenv

*Activando el entorno virtual*

    myvenv\Scripts\activate

Creando un proyecto en django
-----------------------------

    django-admin startproject got


Correr el servidor
-----------------------------

    python manage.py runserver

Crear tablas en nuestra bd
-----------------------------
Como habrás notado, en nuestro archivo settings.py en la parte de **INSTALLED_APPS** tenemos aplicaciones por default que django usa. Entonces nuestras primera migración lo que hará es crear las tablas respectivas de estas apps.

      python manage.py migrate

Verificando cambios en nuestros modelos
---------------------------------------
Cuando agregamos modelos y relaciones entre estas, en nuestro archivo models.py. Es una buena práctica realizar una validación antes que ejecutar alguna migración

    python manage.py check

Realizar un seguimiento de cambios de nuestros modelos
-------------------------------------
En django es obligatorio realizar esta funcionalidad antes de plasmar nuestros modelos como tablas en la base de datos. Esto permitirá hacer un seguimiento de todos los cambios realizados en nuestros modelos.

    python manage.py makemigrations

Luego de ejecutar este comando lo único que faltaría para que nuestros modelos sean tablas es ejecutar el siguiente comando


    python manage.py migrate


## Otros comandos


**mkdir nombre_directorio** -> creas una carpeta con el nombre 'nombre_directorio'  

**cd nombre_directorio** -> ingresas a la carpeta 'nombre_directorio'  

**dir** -> listas las carpetas que están en la carpeta actual (en windows)

**ls** -> listas las carpetas que están en la carpeta actual (en Linux)

Recursos:
------------
[SLIDES utilizados en clase](https://drive.google.com/file/d/0BwzkFJZ3lzGOYkJnZDlTYzhLR1U/view?usp=sharing)  
[Introducción a Django](https://docs.google.com/presentation/d/1cpCbjrA5cv9igtz76xjcyjxMbxnqfrJRu6Xb02LzV98/edit?usp=sharing)  
[Tutorial de Django Girls en español](http://tutorial.djangogirls.org/es/)  
