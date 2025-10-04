import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import date, timedelta

# Es buena práctica incluir un User-Agent para simular un navegador real
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def obtener_datos_clima_tutiempo(url):
    """
    Extrae la tabla de datos climáticos de TuTiempo.net, 
    buscando directamente filas sin depender de <thead>/<tbody>.
    """
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. Localizar la tabla: está dentro de un div con clase 'thh'
        table = soup.select_one('div.thh table')

        if table is None:
            # Si no encuentra la tabla, la página podría estar vacía
            # Esto maneja el error inicial de no encontrar la tabla en la primera pasada
            return None

        # 2. Extraer TODAS las filas de la tabla directamente (<tr>)
        # Esto incluye la fila de encabezado y las filas de datos.
        all_rows = table.find_all('tr')
        
        if not all_rows:
            return None

        # 3. Identificar los encabezados de la segunda fila (la primera es el día, la segunda es la de las columnas)
        # La primera fila (índice 0) contiene "Martes, 2 de Julio de 2024", la segunda (índice 1) contiene los nombres.
        # En el HTML de ejemplo, los nombres de columna son <th> en la segunda <tr>.
        
        # Fila de Encabezados (la segunda fila de la tabla)
        header_row = all_rows[1] 
        headers_raw = [th.text.strip() for th in header_row.find_all('th') if th.text.strip()]

        # Mapeo y ajuste de encabezados (simplificado y basado en el HTML)
        headers = ["Hora", "Condiciones meteorológicas", "Temperatura", "Viento", "Humedad", "Presión", "Punto de rocío"]

        # 4. Extraer datos del cuerpo: las filas comienzan desde la tercera (índice 2)
        data = []
        # Iterar desde la fila 2 en adelante
        for row in all_rows[2:]:
            cells = row.find_all('td')
            if not cells: 
                continue
                
            row_data = []
            
            # Hora (0)
            row_data.append(cells[0].text.strip())
            
            # Condiciones meteorológicas (1)
            # El texto está en un <span> dentro de <td>
            condicion_span = cells[1].find('span')
            row_data.append(condicion_span.text.strip() if condicion_span else "N/A")
            
            # Temperatura (2)
            row_data.append(cells[2].text.strip())

            # Viento (3)
            # El texto del viento tiene un <span> anidado
            wind_span = cells[3].find('span')
            row_data.append(wind_span.text.strip() if wind_span else "N/A")
            
            # Humedad (4), Presión (5), Punto de rocío (6)
            row_data.append(cells[4].text.strip())
            row_data.append(cells[5].text.strip())
            row_data.append(cells[6].text.strip())
            
            data.append(row_data)

        # 5. Crear DataFrame
        df = pd.DataFrame(data, columns=headers)
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL {url}: {e}")
        return None
    except IndexError:
        print(f"Error de índice: La tabla no tiene suficientes filas para la extracción en {url}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado al procesar la URL {url}: {e}")
        return None


# ----------------------------------------------------------------------
## 💻 Función para Iterar y Generar URLs (Dejar sin cambios)
# ----------------------------------------------------------------------

def generar_urls_mensuales(estacion, mes, anio):
    # ... (código para generar URLs) ...
    # Asegúrate de usar esta función de tu script anterior
    meses_es = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", 
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    urls = []
    try:
        if mes == 12:
            ultimo_dia = date(anio + 1, 1, 1)
        else:
            ultimo_dia = date(anio, mes + 1, 1)
    except ValueError:
        ultimo_dia = date(anio, mes, 1) + timedelta(days=28) 

    current_date = date(anio, mes, 1)

    while current_date < ultimo_dia:
        dia = current_date.day
        nombre_mes = meses_es[mes]
        url = f"https://www.tutiempo.net/registros/{estacion}/{dia}-{nombre_mes}-{anio}.html"
        urls.append(url)
        current_date += timedelta(days=1)
        
    return urls

# ----------------------------------------------------------------------
## 🚀 Ejecución del Script
# ----------------------------------------------------------------------

mes_a_extraer = 0

while mes_a_extraer <= 9:
    estacion_cdmx = 'mmmx' # Código ICAO para Ciudad de México
    anio_a_extraer = 2025
    mes_a_extraer += 1

    urls_julio = generar_urls_mensuales(estacion=estacion_cdmx, mes=mes_a_extraer, anio=anio_a_extraer)

    all_data = []
    for url in urls_julio:
        print(f"Intentando extraer datos de: {url}")
        df_dia = obtener_datos_clima_tutiempo(url)
        
        if df_dia is not None and not df_dia.empty:
            fecha_str = url.split('/')[-1].replace('.html', '')
            df_dia.insert(0, 'Fecha_Registro', fecha_str)
            all_data.append(df_dia)
        
        # Pausa de 1 segundo para evitar ser bloqueado
        time.sleep(1) 

    if all_data:
        df_final = pd.concat(all_data, ignore_index=True)
        nombre_archivo = f'clima_cdmx_{mes_a_extraer}_{anio_a_extraer}_historico.csv'
        df_final.to_csv(nombre_archivo, index=False)
        print(f"\n✅ ¡Extracción de {len(all_data)} días completa y guardada en '{nombre_archivo}'!")
        print("\nPrimeras 10 filas del DataFrame:")
        print(df_final.head(10))
    else:
        print("\n❌ No se pudieron extraer datos de ningún día. Verifica la conexión o la estructura de la página.")