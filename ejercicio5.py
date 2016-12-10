cant_notas = input('Ingresar la cantiad de notas: ')
i = 0
acu = 0
while i < int(cant_notas):
	i += 1
	nota = input('Ingresa la nota: ')
	acu += int(nota)

if acu/int(cant_notas) > 10:
	print('Aprobaste!! :D con ', acu/int(cant_notas))
else:
	print('Reprobaste :( con ', acu/int(cant_notas))