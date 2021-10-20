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
7. Insertar su primera dep_ips
      Debe modificar archivos para insertar el primer dep_ips
      
      1) Ir a **pruebaSerializer.py** y quitar 'dep_ips' de la lista llamada fields
      2) Comente la líne **pruebaData.pop("dep_ips")** en el archivo **dep_ipsSerializer.py**
8. Cree el primer dep_ips usando el caso de prueba CreateDep_ipsCorrect empleando postman(Los casos de prueba se agregan al final de este documento)
9. Luego de crear su primer dep_ips deshaga las acciones del paso 7


[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/afca26af1762eb7b3f07?action=collection%2Fimport)
