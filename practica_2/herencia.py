import random

cromosomas = 20
parejas = 50

def gen_padres():
	madre = [[0 for i in range(cromosomas)] for j in range (parejas)]
	padre = [[0 for i in range(cromosomas)] for j in range(parejas)]
	for i in range(parejas):
		for j in range (cromosomas):
			madre[i][j] = random.randint(1,9)
			padre[i][j] = random.randint(1,9)


	return padre, madre



def herencia(padre, madre):
	hijo1 = 
	hijo2 = 

#para evitar que se reproduzcan entre hermanos y generar 
def incesto():
	hermanos = True
	hermano1 = list(range(parejas))
	hermano2 = list(range(parejas))
	while hermanos:
		random.shuffle(hermano1)
		random.shuffle(hermano2)
		hermanos = False
		for i in range(parejas):
			if hermano1[i] == hermano2[i]: 
				hermanos True
	return hermano1, hermano2



def mutacion(hijos):
	for i in range(parejas):
		random.random() < .10: #el minimo, en caso de ser necesario se debe de agregar un poco mas (hasta 25%)
		j = random.randint(0, cromosomas -1 )
		hijos[i][j] = random.randint(1,9)
	return hijos


#para pode encontrar el hijo perfecto (todos los cromosomas con valor de 9). 
def ario(personas):
	return any(all(c == 9 for c in personas) for i in personas)



if __name__ == "__main__":
	padres, madres = gen_padres()
	print(f"Los padres son {padres}")
	print(f"Las madres son {madres}")
	hijo1 , hijo2 = herencia(padres,madres)
	generaciones = 0 
	
	while ario(hijo1) and ario(hijo2): 
		gen += 1
		print(f"Generacion: {gen}\n")
		hijo1, hijo2 = herencia(humanos1, humanos2)
		hijo1 = mutacion(hijo1)
		hijo2 = mutacion(hijo2)

	print(f"Despues de {generaciones} se encontro al hijo perfecto.")




