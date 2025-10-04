import requests
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def baixar_dados(latitude, longitude, start=2023, end=2024):
    url = (
        "https://power.larc.nasa.gov/api/temporal/monthly/point"
        "?parameters=T2M,T2M_MAX"
        "&community=SB"
        f"&longitude={longitude}"
        f"&latitude={latitude}"
        f"&start={start}"
        f"&end={end}"
        "&format=JSON"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def frange(start, stop, step):
    vals = []
    while (step < 0 and start >= stop) or (step > 0 and start <= stop):
        vals.append(round(start, 2))
        start += step
    return vals

# Exemplo de uso:
latitude = -19.92
longitude = -43.94
latitudes = frange(-10.92, -13.27, -0.1)
longitudes = frange(-59.61, -61.09, -0.1)

results = []
for lat in latitudes:
    for lon in longitudes:
        try:
            dados = baixar_dados(lat, lon)
            for year_month, values in dados['properties']['parameter']['T2M'].items():
                print({
                    'latitude': lat,
                    'longitude': lon,
                    'year_month': year_month,
                    'T2M': values,
                    'T2M_MAX': dados['properties']['parameter']['T2M_MAX'][year_month]
                })
                results.append({
                    'latitude': lat,
                    'longitude': lon,
                    'year_month': year_month,
                    'T2M': values,
                    'T2M_MAX': dados['properties']['parameter']['T2M_MAX'][year_month]
                })
        except Exception as e:
            print(f"Erro ao baixar dados para {lat}, {lon}: {e}")

df = pd.DataFrame(results)
df.to_csv('./dados_nasa.csv', index=False)
#dados = baixar_dados(latitude, longitude)
#print(dados)