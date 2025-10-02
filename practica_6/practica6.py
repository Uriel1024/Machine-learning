#importamos las librerias necesarias y los dataset 
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN, Birch, AgglomerativeClustering
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, make_blobs, make_moons
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import seaborn as sns

RANDOM_STATE = 42

#precargamos las variables de los dataset para poder trabajarlos 
path_mall_costumers = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3-zrTL0T9NSuA9BKqrs1JR2UxLI6-faydh4eUo91In88M4DgVaogIxbHeUN0UamV0-j1S25KLbBpg/pub?gid=2104197020&single=true&output=csv"

data_iris = load_iris()
x_iris, y_iris = data_iris.data, data_iris.feature_names

x_blobs, y_blobs = make_blobs(n_samples = 300,centers = 3,cluster_std = 1.0,random_state = RANDOM_STATE)  

x_moons, y_moons = make_moons(n_samples = 300,  random_state = RANDOM_STATE)

df_iris = pd.DataFrame(x_iris, columns=y_iris)
df_blobs = pd.DataFrame(x_blobs)
df_moons = pd.DataFrame(x_moons)



def entrenamiento(data_x, df, dataset):	
	modelos = {
		"KMeans":  KMeans(n_clusters =3, random_state = RANDOM_STATE)
	}	

	for nombre,model in modelos.items():
		model.fit(data_x)
		df['Cluster'] = model.labels_
		silhouette_avg = silhouette_score(data_x,model.labels_)
		print(f"El silhouette_score del dataset {dataset} con el modelo {nombre} es de: {silhouette_avg:.2f}")
		pca = PCA(n_components= 2)
		reduced_data = pca.fit_transform(data_x)

		plt.figure(figsize=(8, 6))
		for cluster in range(3):
		    plt.scatter(
		        reduced_data[model.labels_ == cluster, 0],
		        reduced_data[model.labels_ == cluster, 1],
		        label=f"Cluster {cluster}"
		    )

		# Plot cluster centers
		centers = pca.transform(model.cluster_centers_)
		plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='.', s=200, label='Centroids')

		plt.title(f"{nombre} Clustering en el {dataset} Dataset (PCA Reduced)")
		plt.xlabel("Principal Component 1")
		plt.ylabel("Principal Component 2")
		plt.legend()
		plt.show()




if __name__ == "__main__":

	entrenamiento(x_iris,df_iris,"iris")

	#para mostrar el bobs dataset 
	entrenamiento(x_blobs,df_blobs,"blobs")
	#para mostrar el moon dataset
	entrenamiento(x_moons,df_moons,"moons")

