archivo = open('quijote.txt', encoding='utf-8')
contenido = archivo.read()
archivo.close()

set_contenido = set(contenido)
for a in set_contenido:
	if a not in 'abcdefghijklmnñopqrstuvxwyzABCDEFGHIJKLMNÑOPQRSTUVXWYZ':
		print(a)