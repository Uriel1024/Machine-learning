from sklearn.model_selection import cross_validate, KFold
from sklearn.metrics import  make_scorer
from sklearn.datasets import load_iris, load_breast_cancer, load_wine
#no se especificio que modelo usar para la practica, por lo que se decidio usar dos modelos que ya conocemos 
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data_wine = load_wine()
data_iris = load_iris()
data_breast_cancer = load_breast_cancer()

#cargamos los dataset
datasets = {
"iris" : data_iris, 
"breast_cancer": data_breast_cancer, 
"Wine": data_wine 
}

#funcion para optener las variables de cada dataset
def get_data(data):
	x ,y = data.data, data.target
	return x, y

#para fragmentar la info de cada dataset 
def validacion():
	
	#definimos la funcion de cross validation (se va a dividir el dataset en 5) 
	kf = KFold(n_splits = 5, shuffle = True, random_state = 42)

	modelos = {
	"RandomForestRegressor": RandomForestRegressor(random_state =42),
	"LinearRegression": LinearRegression()
	}

	Modelo_lista =  [] 
	Dataset= []
	MSE= []
	R2=  []
	for nombre, modelo in modelos.items():
		for n_dataset,dataset in datasets.items():
			x, y = get_data(dataset)
			scores = cross_validate(modelo, x, y, cv=kf ,scoring=('r2', 'neg_mean_squared_error'),return_train_score=True)
			mean_mse = np.mean(scores["test_neg_mean_squared_error"])
			mean_r2 = np.mean(scores["train_r2"])
			Dataset.append(n_dataset)
			MSE.append(mean_mse)
			R2.append(mean_r2)
			Modelo_lista.append(nombre)

	resultados_df = pd.DataFrame({
        "Modelo": Modelo_lista,
        "Dataset": Dataset,
        "MSE_Promedio": MSE,
        "R2_Promedio_Train": R2
    })

	return resultados_df 

def graficar_resultados(df):
    # Asegúrate de que los valores de MSE sean positivos para graficar la magnitud
    df['MSE_Positivo'] = -df['MSE_Promedio']

    # --- Gráfico de Barras para R2 Promedio de Entrenamiento ---
    plt.figure(figsize=(10, 5))
    bar_r2 = df.pivot(index='Dataset', columns='Modelo', values='R2_Promedio_Train')
    bar_r2.plot(kind='bar', ax=plt.gca())

    plt.title('R² Promedio (Train) por Modelo y Dataset')
    plt.ylabel('R² Promedio (Train)')
    plt.xticks(rotation=0)
    plt.legend(title='Modelo')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
    # 

    # --- Gráfico de Barras para MSE Promedio (Test) ---
    plt.figure(figsize=(10, 5))
    bar_mse = df.pivot(index='Dataset', columns='Modelo', values='MSE_Positivo')
    bar_mse.plot(kind='bar', ax=plt.gca())

    plt.title('MSE Promedio (Test) por Modelo y Dataset')
    plt.ylabel('MSE Promedio (Test) - Magnitud')
    plt.xticks(rotation=0)
    plt.legend(title='Modelo')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
    # 


if __name__ == '__main__':
	resultados = validacion()
	graficar_resultados(resultados)