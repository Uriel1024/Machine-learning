import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.utils import Bunch
from skimage.io import imread_collection, imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
import os
import glob 
from pathlib import Path
#para no tener problemas con las rutas gg
BASE_DIR = Path(__file__).resolve().parent.parent
path  = BASE_DIR /"practica_9/frutas/train"

#para poder usar un tamanio estandar de las imgs  y pasarlas a vectores 
def segmentacion(dim = (300,300)):
	#para guaradar las carpetas 
	carpetas = [nombre for nombre in os.listdir(path) if  os.path.isdir(os.path.join(path, nombre))]
	imgs = [img for img in glob.glob(str(path) + "/*/*.jpg")]
	carpetas.sort()
	#listas para guardar los datos
	images = []
	data = []
	target = []
	#recorremos las carpetas e imagenes para poder crear el dataset numerico
	for j in imgs:
		try:
			imagen = imread(j)
			height, width = imagen.shape[:2]

			if imagen.ndim == 2: # Es escala de grises
				# Convierte a color replicando el canal
				imagen = np.stack((imagen,)*3, axis=-1) 
			elif imagen.ndim == 4: # Es RGBA (con canal alfa)
				# Elimina el canal alfa
				imagen = imagen[:, :, :3]

			#las img muy peqenias no se pueden redimensionar bien
			if height < 300 and width < 300:
				print(f"la imagen {j} es demasiado pequenia y se omite")
				continue
			imagen = resize(imagen, dim)
			images.append(imagen)
			data.append(imagen.flatten())
			target.append(carpetas.index(os.path.basename(os.path.dirname(j))))

			nombre_clase = os.path.basename(os.path.dirname(j))
			print(f"procesada la imagen {j} de la clase {nombre_clase}")
	
		except ValueError:
			print(f"error, la clase {nombre_clase} no se encuentra en las carpetas")
			continue
		except Exception as e:
			print(f"error al procesar la imagen {j}: {e}")
			continue
	print(f"Total de imgs procesaedas es de:{len(data)}")
	
	#devolvemos un objeto tipo bunch con los datos

	return Bunch(data = np.array(data), target = np.array(target), images = np.array(images), target_names = carpetas)

if __name__ == '__main__':
	data = segmentacion()
	print(data.data.shape)	


