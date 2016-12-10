#--- cuantas veces aparece cada caracter
archivo = open('quijote.txt', encoding='utf-8')
contenido = archivo.read()
archivo.close()
diccionario = {}
for a in contenido:
	if diccionario.get(a) != None:
		diccionario[a] += 1
	else:
		diccionario[a] = 1
items = list(diccionario.items())
items.sort(key=lambda i: i[1], reverse=True)

print(items)