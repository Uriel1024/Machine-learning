from sklearn.metrics import mean_squared_error,  	r2_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from datetime import datetime

#precargamos el dataset y eliminamos las columnas que no aportan nada, tambien nos encargamos de  
path =  "https://docs.google.com/spreadsheets/d/e/2PACX-1vQydOdg2J0J4AYLkY4kwiu74TbhdZFESHlxU-3TIAb7aC_OMzjwHjPLRb3Zlc718qwGVeo1v58PGQr0/pub?gid=1201603970&single=true&output=csv"
data = pd.read_csv(path)

#Diccionario que contiene el nombre de la columna con el caracter que se va a elimnar 
columnas_info = {
	"Temperatura": r'\s?°',
	"Viento": r'\s?km/h',
	"Humedad": r'\s?%',
	"Presión": r'\s?hPa',
	"Punto de rocío":  r'\s?°' 
}

def limpiar_datos(df,columnas_info):
	for columna, imp in columnas_info.items():
		df[columna] = df[columna].astype(str).str.replace(imp,'',regex = True)
		df[columna] = pd.to_numeric(df[columna], errors='coerce')
	return df


  
if __name__ == "__main__":
	data = 	limpiar_datos(data,columnas_info)


