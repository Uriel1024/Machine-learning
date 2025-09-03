import random

cromosomas = 20
parejas = 50 

def gen_padres():
	madre = [[0 for _ in range(cromosomas)] for _ in range (parejas)]
	padre = [[0 for _ in range(cromosomas)] for _ in range(parejas)]
	for i in range(parejas):
		for j in range (cromosomas):
			madre[i][j] = random.randint(1,9)
			padre[i][j] = random.randint(1,9)
	return padre, madre

def herencia(padre, madre):
    # Cruza los cromosomas de los padres para crear dos hijos con promedios
    hijo_1 = [
        [(padre[i][j] + madre[i][j]) // 2 for j in range(cromosomas)]
        for i in range(parejas)
    ]
    hijo_2 = [
        [((padre[i][j] + madre[i][j]) + 1) // 2 for j in range(cromosomas)]
        for i in range(parejas)
    ]
    return hijo_1, hijo_2



padre, madre = gen_padres()
hijo1 , hijo2 = herencia(padre,madre)

print(f"Padre 1: {padre}\n\n\n")
print(f"madre 1: {madre}\n\n\n")

print(f"Hijo 1: {hijo1}\n\n\n")
print(f"Hijo 2: {hijo2}")
