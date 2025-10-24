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
import requests



path = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQtBR2e1693fbkbllA5XrTd5cnCZoDRJa4TQQKEbmEON-UQEPtox7fv69uuoVY9dHbnKSaOEwuwICRI/pub?gid=921974745&single=true&output=csv"
data = pd.read_csv(path)

latitud = 19.4829
longitud = -99.1135
RM = 42
API_URL = "https://api.open-meteo.com/v1/forecast" 

def obtener_pronostico_openmeteo(fecha_hora: str):
    start_date = pd.to_datetime(fecha_hora).strftime('%Y-%m-%d')
    
    params = {
        'latitude': latitud,  # <-- Change from LATITUD
        'longitude': longitud, # <-- Change from LONGITUD
        'hourly': 'relative_humidity_2m,dew_point_2m', 
        'timezone': 'America/Mexico_City',
        'start_date': start_date,
        'end_date': start_date,
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status() # Lanza un error si el código de estado es 4xx o 5xx
        data = response.json()
        
        # Convertir el resultado a un DataFrame para buscar la hora exacta
        hourly_data = pd.DataFrame({
            'time': pd.to_datetime(data['hourly']['time']),
            'relative_humidity_2m (%)': data['hourly']['relative_humidity_2m'],
            'dew_point_2m (°C)': data['hourly']['dew_point_2m'],
        })
        
        # Buscar el pronóstico para la hora solicitada
        target_time = pd.to_datetime(fecha_hora).replace(minute=0, second=0)
        
        pronostico = hourly_data[hourly_data['time'] == target_time]
        
        if not pronostico.empty:
            humedad = pronostico['relative_humidity_2m (%)'].iloc[0]
            punto_rocio = pronostico['dew_point_2m (°C)'].iloc[0]
            return humedad, punto_rocio
        else:
            print(f"Error: No se encontró pronóstico para la hora exacta: {target_time}")
            return None, None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Open-Meteo: {e}")
        return None, None
 

data['time'] = pd.to_datetime(data['time'])
data['day_of_year'] = data['time'].dt.dayofyear
data['hour'] = data['time'].dt.hour

features = ['day_of_year', 'hour', 'precipitation (mm)', 'rain (mm)',
            'relative_humidity_2m (%)', 'dew_point_2m (°C)']
x = data[features].copy()
y = data['temperature_2m (°C)']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2,random_state=RM)

def entrenamiento():
    model = RandomForestRegressor(n_estimators=100, max_depth= 6, random_state=RM)
    #modelo   = RandomForestRegressor(max_depth = 6, random_state = RM)
    #modelo = KNeighborsRegressor()
    #modelo = LinearRegression()

    model.fit(x_train, y_train)
    rest = {"Modelo ": [], "R2": [], "MSE": []}
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    rest["Modelo "].append("Random Forest Regressor")
    rest["R2"].append(r2)
    rest["MSE"].append(mse)

    return model, pd.DataFrame( rest)


def predecir_temperatura(modelo, fecha_hora):
    fecha_dt = pd.to_datetime(fecha_hora)

    humedad_pred, punto_rocio_pred = obtener_pronostico_openmeteo(fecha_hora)
    
    if humedad_pred is None:
        return "No se pudo obtener el pronóstico de la API para hacer la predicción."

    day_of_year = fecha_dt.dayofyear
    hour = fecha_dt.hour

    nueva_entrada = pd.DataFrame({
        'day_of_year': [day_of_year],
        'hour': [hour],

        'precipitation (mm)': [0.0],  
        'rain (mm)': [0.0],
        'relative_humidity_2m (%)': [humedad_pred],
        'dew_point_2m (°C)': [punto_rocio_pred]
    })

    column_order = ['day_of_year', 'hour', 'precipitation (mm)', 'rain (mm)',
                    'relative_humidity_2m (%)', 'dew_point_2m (°C)']
    nueva_entrada = nueva_entrada[column_order]

    temperatura_pred = modelo.predict(nueva_entrada)[0]  

    print(f"-> Características de entrada: Día del año={day_of_year}, Hora={hour}, Precipitación=0.0mm, Lluvia=0.0mm, Humedad={humedad_pred}%, Punto Rocío={punto_rocio_pred}°C")
    return temperatura_pred

def obtener_hora():
    """Obtiene la hora actual (redondeada a la hora más cercana para la API)."""
    now = datetime.now()
    rounded_hour = now.replace(minute=0, second=0, microsecond=0)
    if now.minute >= 30:
        rounded_hour += pd.Timedelta(hours=1)
    return rounded_hour.strftime('%Y-%m-%dT%H:%M')

if __name__ == "__main__":    
    modelo, resultados  = entrenamiento()

    print("--- Resultados del Entrenamiento ---")
    print(resultados)

    fecha_a_predicir = obtener_hora()
    print(f"\nLa fecha y hora para predecir (usando el pronóstico de la API) es: {fecha_a_predicir}")

    temperatura = predecir_temperatura(modelo, fecha_a_predicir)
    
    if isinstance(temperatura, (float, np.float64)):
        print(f"\n**Temperatura PRONOSTICADA es de: {temperatura:.2f} °C**")
    else:
        print(f"\n{temperatura}")