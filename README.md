# Prueba Django

_Prueba realizada para CiberC Latam_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Proyecto probado en ubuntu 18.04
Python 3.7
Django 2.2
Mysql 8
```

### Instalación 🔧

_Ejecutar los siguientes pasos_


```
1. Clonar el repositorio
2. Ingresar a la carpeta examen
3. ejecutar:  source bin/activate
4. instalar:  pip3 install -r requirements.txt
5. instalar Mysql 8
6. editar los accesos de bd:  examen/inventario/inventario/settings.py
7. ingresar examen/inventario
8. ejecutar  sudo python3 manage.py makemigrations inv
9. ejecutar  sudo python3 manage.py migrate inv
10. ejecutar  sudo python3 manage.py createsuperuser
11. ejecutar  sudo python3 manage.py runserver
```

### Pruebas

_Ejecutar los siguientes pasos_


```
1. Dentro de la carpeta examen/inventario hay un archivo llamado test.xlsb
   que contiene data de prueba, con tres columnas serie, cantidad y precio.
2. Dentro del admin hay un modelo llamado Carga, donde podemos importar el archivo test.xlsb
3. en el index hay un boton llamada items, donde podemos dar click y visualizar la data cargada.
```
