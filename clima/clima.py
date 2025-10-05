from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from datetime import datetime




#normaliza los datos 
def limpiar_datos(df):
	#Diccionario que contiene el nombre de la columna con el caracter que se va a elimnar 
	columnas_info = {
		"Temperatura": r'\s?°',
		"Viento": r'\s?km/h',
		"Humedad": r'\s?%',
		"Presión": r'\s?hPa',
		"Punto de rocío":  r'\s?°' 
	}
	for columna, imp in columnas_info.items():
		df[columna] = df[columna].astype(str).str.replace(imp,'',regex = True)
		df[columna] = pd.to_numeric(df[columna], errors='coerce')
	return df

#precargamos el dataset   
path =  "https://docs.google.com/spreadsheets/d/e/2PACX-1vQydOdg2J0J4AYLkY4kwiu74TbhdZFESHlxU-3TIAb7aC_OMzjwHjPLRb3Zlc718qwGVeo1v58PGQr0/pub?gid=1201603970&single=true&output=csv"
data = pd.read_csv(path)

#eliminamos las columnas innecesarias
data = data.drop(columns = "Condiciones meteorológicas")

cols_to_drop = [col for col in data.columns if col.startswith('Unnamed:')]
data = data.drop(columns=cols_to_drop)


data = limpiar_datos(data)

#random_state = 42, por si se quiere cambiar para ver si el modelo tiene resultado diferente
RM = 42

#Limpiamos los datos antes de particionar para el modelo
data = 	limpiar_datos(data)

#dividimos  80/20 el dataset 
target = "Temperatura"
excluidas = ['Fecha_Registro', 'Hora','Timestamp', target]
x = data.drop(columns=excluidas, errors = 'ignore')
y = data[target]



#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2, random_state = RM)
# Entrenamiento: Filas antiguas (80% del inicio)
train_size = int(0.8 * len(data))

x_train = x.iloc[:train_size] 
y_train = y.iloc[:train_size] 

# Prueba: Filas más recientes (20% del final)
x_test = x.iloc[train_size:]  
y_test = y.iloc[train_size:]

def entrenamiento():
	RMR = RandomForestRegressor(max_depth = 6, random_state = RM)
	RMR.fit(x_train, y_train)
	y_pred = RMR.predict(x_test)

	return  mean_squared_error(y_test, y_pred) ,r2_score(y_test, y_pred)


  
if __name__ == "__main__":
	mse, r2 = entrenamiento()
	print(f"\nEl MSE del modelo es: {mse}")
	print(f"\nEl r2 del modelo es: {r2}")

