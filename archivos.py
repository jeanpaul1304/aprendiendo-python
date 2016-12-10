with open('quijote.txt') as archivo:
	quijote = archivo.read()
	#quijote = archivo.readlines()

with (open('salida.txt', 'w') as archivo:
	archivo.write('Lo que quieres guards')