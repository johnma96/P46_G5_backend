# P46_G5_backend
Project for the backend of the programming component of cycle 3 of the MisionTic2022 program

## Instalación en local
1. Luego de clonar el repositorio, ingresar a la carpeta authApp y eliminar la carpeta *migrations*
2. En la raíz del proyecto crear un entorno de python y activarlo
    - python -m venv env
    - source env/bin/activate (Linux)
3. Instalar las dependencias
    - pip install -r requirements.txt
4. Generar las migraciones de la aplicación 
    - python manage.py makemigrations authApp
5. Ejecutar las migraciones para la creación del MER en una base de datos denominada *covid_db*
    - python manage.py migrate
6. Agregar al menos 1 ips y 1 departamento a las tablas usando sql:
    - INSERT INTO "authApp_departamento"(name) VALUES ('Cundinamarca');
    - INSERT INTO "authApp_ips"(name) VALUES ('Salud total');
7. Iniciar la aplicación desde la carpeta raíz
    - python manage.py runserver
    - Nota: Asegúrese que el archivo **manage.py**, en la línea **os.environ.setdefault...**, tiene al final **settings** y NO **settings_prod**(este settings_prod es para hacer el despliegue usando heroku)
8. Insertar su primera dep_ips

      Debe modificar archivos para insertar el primer dep_ips
      
      1) Ir a **pruebaSerializer.py** y quitar 'dep_ips' de la lista llamada fields
      2) Comente la líne **pruebaData.pop("dep_ips")** en el archivo **dep_ipsSerializer.py**
      3) Cree el primer dep_ips usando el caso de prueba CreateDep_ipsCorrect empleando postman(Los casos de prueba se agregan al final de este documento)
   
9. Luego de crear su primer dep_ips deshaga las acciones del paso 8

## Desplegar la app usando heroku
1. Crear una cuenta en heroku

### Despliegue de la base de datos en remoto
2. Crear una aplicación para la base de datos en heroku
3. Configurar el proyecto para que trabaje con la base de datos de heroku
    - Estando con su aplicación en local genere una copia del archivo **settings.py**, que se encuentra en **authProject**, llamada **settings_prod.py**
    - En settings_prod.py cambie el valor de DEBUG a False y en ALLOWED_HOST coloque en la lista 'localhost'
    - Conecte la base de datos que creó a través de una app como dbeaver empleando las credenciales de heroku
    - Use las mismas credenciales para cambiar los valores de DATABASES en **settings_prod.py**
    - Modifique el archivo **manage.py**: En la línea **os.environ.setdefault...** ingrese al final **settings_prod**
    - Modifique el archivo **wsgi.py**: En la línea **os.environ.setdefault...** ingrese al final **settings_prod** (Nota: este cambio no afecta la instalación en local)
4. Generar las migraciones de la aplicación 
    - python manage.py makemigrations authApp
5. Ejecutar las migraciones para la creación del MER en la base de datos de heroku
    - python manage.py migrate
Nota: Si verifica dbeaver debe estar conectado a la base de datos remota y debería tener las tablas de la aplicación creadas

### Despliegue del backend en remoto por primera vez
6. Instalar heroku en su máquina local
    - **sudo snap install --classic heroku** (linux). Otro SO: https://devcenter.heroku.com/articles/heroku-cli
7. Crear una aplicación en heroku para el backend
8. Ir a requirements.txt de la aplicación (authApp) y agregar:
    - gunicorn
    - django_heroku
9. Agregar django_heroku en **settings_prod.py**
    - **import django_heroku** para importar la libreriía
    - Al final del archivo colocar: **django_heroku.settings(locals())
10. En la raíz del backend crear un archivo con nombre **Procfile** y agregarle la línea:
    - web: gunicorn authApp.wsgi
11. Desde terminal estando en la raíz del backend
    - **heroku login** este comando entrega un link que debe usarse en el navegador en el cual esté logueado a heroku para logearse. Luego de logearse, en la terminal debe obtener un msj tipo **...Logged in as pepito@gmail.com** 
12. Conectar la aplicación con heroku
    - heroku git:remote -a <nombre_aplicación_backend>
13. Subir los cambios de la rama de producción en la cual ha estado trabajando o la rama main(La que contenga los cambios anteriores) y subirlo a su repositorio de github
14. En terminal crear una rama master, moverse a ella y copiar el código actualizado de la rama que contenga los cambios de los pasos anteriores
    - git checkout -b master
    - git pull origin main
15. Verifique que todo en la rama master este con commit
    - **git status** debe aparecer sin cambios, de no ser así haga el commit
16. Enviar la aplicación a heroku
    - git push heroku master
17. En heroku, aplicación del backend, pestaña *resources*: eliminar la base de datos que se crea por defecto
    Nota: **¡CUIDADO!:** No es eliminar la aplicación que contiene la base de datos que se creó en el paso 2
18. En heroku dar click eh **Open app** y copiarse la url de la pestaña que abre

### Probar los casos de prueba
19. Genere un fork de los casos de prueba que estaban en local.
20. Cambie, en los casos de prueba copiados, el inicio **localhost:8000/** por la url del paso 18(En la parte inferior están los casos de prueba con la url del paso 18. En caso de que la url sea diferente se debe cambiar)
21. En el archivo **settings_prod.py** agregue a ALLOWED_HOSTS la url que obtuvo. Debe quedar tipo:

    - ALLOWED_HOSTS = ['localhost', 'https://p46g5be.herokuapp.com/']
 
22. Realize un commit del cambio y use el comando del paso 16 para volver a enviar los cambios a heroku
23. Para otras aplicaciones desarrolladas sus casos de prueba ya deben estar corriendo. En el caso de esta aplicación ***authApp*** debe:

        1) Conectarse a la base de datos remota desde terminal
            - psql -U USER_NAME_DB -h HOST -p 5432 NAME_DB  (Use las credenciales de heroku para conectarse)
        3) Agregar al menos 1 ips y 1 departamento a las tablas usando sql:
            - INSERT INTO "authApp_departamento"(name) VALUES ('Cundinamarca');
            - INSERT INTO "authApp_ips"(name) VALUES ('Salud total');
        4) Realizar el paso 8 del despliegue local (Verifique que estos cambios los haga estando en la rama master, recuerde que para crear la primera dep_ips en remoto debe usar el caso de prueba con la url de la aplicación del backen en heroku del paso 18)
        5) Enviar los cambios a heroku. Paso 16 de despliegue de la app usando heroku
        6) Realizar el paso 9 del desplegue local (Verifique que estos cambios los haga estando en la rama master)
        7) Enviar los cambios a heroku. Paso 16 de despliegue de la app usando heroku

### Despliegue del backend en remoto luego de haber desplegado la app por primera vez
1. Instalar heroku(Paso 5 del despliegue por primera vez)
2. Conectar la aplicación ***authApp*** con remoto(Paso 12 del despliegue por primera vez)
3. Realize los cambios de la aplicación ***authApp***
4. Luego de hacer cambios en ***authApp*** asegúrese de que dichos cambios estén en la rama **master**
5. Desde master ejecute:
    - git push heroku master

Nota: Si por alguna razón tiene que eliminar las tablas de la base de datos en heroku, ejecute los pasos 4,5 y 23 del despliegue por primera vez


- [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.postman.co/run-collection/1437556d6999f74cd7c1?action=collection%2Fimport) **Casos de prueba en local**
- [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.postman.co/run-collection/95d27bac85feb1ededee?action=collection%2Fimport) **Casos de prueba en remoto**

