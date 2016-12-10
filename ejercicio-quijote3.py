import re
import json
import io
archivo = open('quijote.txt', encoding='utf-8')
contenido = archivo.read()
archivo.close()
text =contenido
diccionario = {}

text = re.sub(r'[^\w \n]','',text).replace("\n"," ")
words = text.replace("  "," ").split(" ")
for a in words:
	if diccionario.get(a) != None:
		diccionario[a] += 1
	else:
		diccionario[a] = 1
items = list(diccionario.items())
items.sort(key=lambda i: i[1], reverse=True)

print(items[:30])