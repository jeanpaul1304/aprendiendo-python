# Notas clase

##Introduccion

Pip: El npm de Python
bpython e ipython: Mejora la consola - instala con ```pip3 install bpython```
Python para todos: Libro de python en español
RFC: Pep8 es la guia de estilos oficial de python
Booleanos: True y False, con la primera mayuscula
```import math``` Se importa el modulo math
```dir(math)``` Describe que contiene math
```math.pi``` Imprime pi
```str(123)``` Parsea a string
```int('123')``` Parsea a int
```int('123',16)``` Parsea a base 16
```'hola'[1]``` Te hace el corte en la posicion 1
```'hola como estas'[1:4]``` Te hace el corte desde 1 hacia 4
```'Hola'[:4]``` Corta hasta el 4
```'Hola'[4:]``` Corta desde el 4
```'Hola como esta'[1:4:2]``` Corta desde 1 al 4 y salta de 2 en 2
```'Hola como estas'[::-1]``` Revierte la cadena
```'Hola como estas'[:]``` La cadena del inicio al final

## Modulos
Para crear un modulo se necesita crear un archivo y agregarle __init__.py
``` from matematicas import constantes ``` Importa constates desde matematicas
``` from matematicas.constantes import pi ``` Importa pi desde matematicas.constates

## Condicioneles
``` if True : ``` Condicional seguido de :
``` elif condiciona != condiconal : ``` Condicional else if
``` variable = True if 1 > 2 else False ``` If ternario

## Listas

```lista = [1,2,3,variable,'casa']```
```lista.append('algo')``` Se le puede agregar un elento as
```lista.pop()``` Pop devuelve el ultimo elemento y lo quita de la lista
```lista.reverse()``` Invierte el sentido de la lista
```'ingrese la nota numero {}'.format(3)``` El format reemplaza lo que hay en la variable
```'Ingrese la nota numero {0}'.format(3)``` El format reemplaza lo que hay en la variable y tambien se puede numerar

## Diccionarios
``` dictionary = {'perro':'guau', 'gato':'miau'} ``` No funciona como un objeto de js

## Tuplas
``` l = (1,'a') ``` Es un par iterable
``` a,b = l ``` Entonces a = 1 y b = 'a'
```enumerate([a,b,c]) ``` Crea tuplas con posicion y elemento 

## Consuntos o sets
``` conjunto = {1,2,3,4,5} ``` estos funcionan como conjuntos de matematica
``` conjunto.add(7) ``` estos funcionan como conjunto y lo agrega solo si este ya no existe
``` conjunto.union({5,6,8}) ``` Devuelve 1,2,3,4,5,6,8

```'2' in 'abc'``` false
```'a' in 'abc'``` true

## Tools
http://repl.it interprete de python online
mcachayt@gmail.com Moises Cachay

## Cadenas

```arr = "hola, como estas".split(",")``` ```arr = ["hola","como estas"]``` 
```arr = "hola, como estas".upper()``` ``` arr = "HOLA, COMO ESTAS" ``` 
```arr = "HOLA, COMO ESTAS".lower()``` ``` arr = "hola,como estas" ```
```arr.replace("hola,","hey!")``` ```arr = "hey! como estas"```

## Regex
Debes importar el modulo re
re.match busca la primera coincidencia que concida con lo que tu expresion regular representa:
### re.match
Trata de hacer un match :troll:
```re.match(r'\d,'123132123')``` Evalua 1 digito
```re.match(r'\d+,'123123123')``` Evalua de un digito a mas
```re.match(r'\d*', '987654321') ``` Hace match los digitos | r elimina los saltos de linea
```re.match(r'\d{8}', '987654321') ``` Captura los primeros 8 caracteres 
```re.match(r'\d{2,8}','1212121212') ``` Captura ese rango de caracteres
```re.match(r'\^d{8}', '1231231231231')``` ^ = Inicio de cadena
```re.match(r'\d{8}$', '1231231231231')``` $ = fin de cadena
```re.match(r'\d{8}w$', '12312312K')``` w = Pide que tenga al menos un caracter
```re.match(r'\d{8}w?$','12312312')``` w? = Lo vuelve opcional
```re.match(r'\d{8}#?$','12312312#')``` # = Recive simbolos
```re.match(r'\d{8}[\w#]?$','12312312')``` [] = lo vuelve 1 bloque
```w+``` de una letra a mas
```d+``` de un digito a mas
```.``` cualquier caracter
```.+``` de un caracter cualquiera a mas
```W``` Lo inverso a ```w```
```D``` Lo inverso a ```d```
```u'123ñ123'```` Permite usar un elemento unicode como la ñ o emoticones
```^``` Tambien significa negaci'on
```re.match(r'^[^m]\w+$','mama')``` No devuelve nada por que comienza con m
```re.match(r'^(pre|co|al|se)(\w+)$','semilla').group()``` Devuelve los grupos de la expresion regular

### re.sub
Es un replace con estrogenos
```re.sub(r'K|J','', 'J12312312') #~ 12312312 ``` Reemplaza lo que encuentre en la expresion regular

## random
```random.random()``` Te devuleve un numero aleatorio
```random.seed("semilla")``` Le agrega una semilla que permite que los rand sigan la misma secuencia
```random.seed("jeanpaul")``` Los random de estos se repetien, has la prueba

## Iteradores
``` for i in range(10):
		print(i)
	else:
		print('al final')
``` El else se ejecuta al final de la iteracion

## Funciones
``` def suma(*valores):
		return sum(valores)
	print(suma())``` Los valores puede ir definidos con un valor por defecto, tambien puedes poner *variable para indicar varios elementos relacionados a un iterable
```	def suma(*valores, **otros_valores):
		return sum(valores)
	print(suma(1,2,3,4,nombre1='1',nombre2='b'))``` La variable con doble asterisco se convierten en un diccionario