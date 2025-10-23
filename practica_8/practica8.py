from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from datetime import datetime
from IPython.display import display
from datetime import datetime

#link para cargar el dataset de info 

path  = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS8OmjUXLoRFS9QAXSjoSOoZf2Jq23hB01r84dY8WKqVO5ZHWQSIrYJZ_SwfOVJF_WFC0bOgO7A2Rr1/pub?gid=745592261&single=true&output=csv"
data = pd.read_csv(path)

RM = 42
data['time'] = pd.to_datetime(data['time'])


#Las caracteristicas numericas en otro formato 
data['day_of_year'] = data['time'].dt.day_of_year
data['hour'] = data['time'].dt.hour
x = data[['day_of_year', 'hour']]
y = data['temperature_2m (°C)']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2,random_state=RM)


#funcion para entrenar los modelos 
def entrenamiento():
	
	#modelo   = RandomForestRegressor(max_depth = 6, random_state = RM)
	#modelo = KNeighborsRegressor()
	#modelo = LinearRegression()	
    
	modelo =  MLPRegressor(max_iter=2000,random_state=RM)


	rest = {"Modelo": [], "R2": [], "MSE": []}
	modelo.fit(x_train, y_train)
	y_pred = modelo.predict(x_test)
	r2 = r2_score(y_test,y_pred)
	mse = mean_squared_error(y_test,y_pred)

	rest["Modelo"].append("Random Forest Regressor")
	rest["R2"].append(r2)
	rest["MSE"].append(mse)


	return pd.DataFrame(rest), modelo 

def predecir_temperatura(modelos, fecha_hora):
	fecha_hora = pd.to_datetime(fecha_hora) 

	day_of_year = fecha_hora.dayofyear
	hour = fecha_hora.hour

	nueva_entrada = pd.DataFrame({
		'day_of_year': [day_of_year],
		'hour': [hour]
	})
	
	prediccion = modelo.predict(nueva_entrada)	

	return prediccion[0]
	
def obtener_hora():
	ahora = datetime.now()
	dia_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
	return dia_hora

if __name__ == "__main__":
	resultados, modelo  = entrenamiento()

	print("--- Resultados del Entrenamiento ---")
	display(resultados)

	fecha_a_predicir = obtener_hora()
	print(f'La fecha y hora para predecir el clima es: {fecha_a_predicir}')

	temperatura = predecir_temperatura(modelo,fecha_a_predicir)
    
	print(f"Temperatura es de : {temperatura:.2f} °C")
