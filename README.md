# Desarrollo 2
En el siguiente repositorio, se encuentra la solucion al siguiente requerimiento

_Dado el servicio web creado, en el lenguaje/librería/framework que prefiera, desarrollar una aplicación web que:_
* _Acepte un número desde un textbox. Validar que este número sea un entero positivo distinto de 0._
* _Tomando como parámetro el número previamente validado, crear un botón que invoque el servicio web vía HTTP, e imprimir en pantalla el término n-ésimo término de la sucesión de Fibonacci._
## Instalacion
La solución fue implementada en Python3.8 usando `virtualenv` en Linux.
Por esto, se deben instalar lo siguiente:
```shell script
$ sudo apt install python-virtualenv virtualenv
$ virtualenv venv --python=python3
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Luego, para levantar el servicio:
```shell script
(venv) $ python app.py
```
Y para ejecutar los test unitarios:
```shell script
(venv) $ python test_app.py
```
