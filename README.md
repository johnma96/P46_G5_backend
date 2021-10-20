# P46_G5_backend
Project for the backend of the programming component of cycle 3 of the MisionTic2022 program
Test https://orange-crater-532875.postman.co/workspace/32ce41ea-5eb7-4a87-8c96-f30c9a179025/request/17935111-f3b2d8ac-1f24-4586-b830-77272fa4c200


Para que funcione primero tiene que agregar al menos 1 ips y 1 departamento a las tablas usando
sql:
- INSERT INTO "authApp_departamento"(name) VALUES ('Cundinamarca');
- INSERT INTO "authApp_ips"(name) VALUES ('Salud total');

Luego debe ir al archivo mover algunos archivos para insertar el primer dep_ips
1. Ir a pruebaSerializer.py y quitar 'dep_ips' de la lista llamada fields
2. Comente la líne pruebaData.pop("dep_ips") en el archivo dep_ipsSerializer.py

Luego de crear su primer dep_ips deshaga los pasos anteriores

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/afca26af1762eb7b3f07?action=collection%2Fimport)
