nota_1 = input("Ingrese nota 1:")
nota_2 = input("Ingrese nota 2:")
nota_3 = input("Ingrese nota 3:")
nota_4 = input("Ingrese nota 4:")
nota_5 = input("Ingrese nota 5:")
total = 0
for nota in [nota_1,nota_2,nota_3,nota_4,nota_5]:
	total += int(nota)

promedio = total/5

if promedio > 10:
	print('Aprobaste!! :D con ', promedio)
else:
	print('Reprobaste :( con ', promedio)