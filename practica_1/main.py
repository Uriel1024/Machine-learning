import os
from diccionario import pensamiento
from diccionario import preguntas
from diccionario import caracteristicas
from collections import Counter



#esta funcion es para saber es la caracteristica que mas se repite y poder hacer las preguntas
def pregunta_optima():
	contador = Counter()

	for elemento , caracteristicas_objeto in pensamiento.items():
		for caracteristicas, valor in caracteristicas_objeto.items():
			if valor:
				contador[caracteristicas] += 1
	mas_comun = contador.most_common(1)
	print("\nLa caracteristica mas comun es: ", mas_comun[0][0])
	return mas_comun[0][0]	

#funcion para hacer las preguntas
def hacer_preguntas(best_q):



best_q = pregunta_optima()
hacer_preguntas(best_q)



