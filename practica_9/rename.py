#este archivo es para renombrar las imagenes de todas las carpetas
import os 
from pathlib import Path
import string	

BASE_DIR = Path(__file__).resolve().parent.parent
directory = BASE_DIR /"practica_9/pomegranate"

def directorion():
	directorios = []
	with os.scandir(directory) as ficheros:
		for fichero in ficheros:
			if fichero.is_dir():
				directorios.append(fichero.name)


	for i in directorios:
		carpeta = f"{directory}/{i}"
		for j, imagen in enumerate(os.listdir(carpeta), start = 1):
			old_path = os.path.join(carpeta,imagen)
			new_path = os.path.join(carpeta, f"img_{j}.jpg")

			os.rename(old_path, new_path)	
		#	print(f"Imagen renombrada de {old_path} a {new_path}")
		print(f"Se renombraron las imgs de la carpeta {carpeta}")

def directorio1():
	iterador = 0
	carpeta = directory
	for j, imagen in enumerate(os.listdir(carpeta), start = 11):
		old_path = os.path.join(carpeta,imagen)
		new_path = os.path.join(carpeta, f"img_{j}.jpg")

		os.rename(old_path, new_path)	
		print(f"Imagen renombrada de {old_path} a {new_path}")
		iterador += 1
	print(f"Se renombraron las imgs de la carpeta {carpeta}, con un total de {iterador}")





if __name__ == '__main__':
	a = input("Ingresa la cantidad de carpetas:")

	if a == '1':
		directorio1()
	else:
		directorion()