def suma(*valores):
	return

print(suma())


def other_sum(uno,dos,tres,cuatro):
	return uno + 2

numeros = [1,2,3,4]
print(other_sum(*numeros))

otros_numeros = {'uno':1,'dos':2,'tres':3,'cuatro':4}
print(other_sum(**otros_numeros))