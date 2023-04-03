import numpy as np
import pandas as pd

# Configuración de la forma de onda
amplitud = 330.0
frecuencia = 60.0  # en Hz
fase1 = np.deg2rad(0)  # fase desplazada 30 grados
fase2 = np.deg2rad(45)  # fase desplazada 30 grados
fase3 = np.deg2rad(90)  # fase desplazada 30 grados

# Generación de las muestras
num_muestras = 1000
tiempo_inicial = 0.0
tiempo_final = 0.2  # en segundos
tiempos = np.linspace(tiempo_inicial, tiempo_final, num_muestras)

# Generación de la onda cosenoidal desplazada
onda1 = amplitud * np.cos(2*np.pi*frecuencia*tiempos + fase1)
onda2 = amplitud * np.cos(2*np.pi*frecuencia*tiempos + fase2)
onda3 = amplitud * np.cos(2*np.pi*frecuencia*tiempos + fase3)

# Redondeo de los valores de la onda a enteros
onda_entera1 = np.round(onda1).astype(int)
onda_entera2 = np.round(onda2).astype(int)
onda_entera3 = np.round(onda3).astype(int)

# Almacenamiento de las muestras en un array
voltajes1 = np.array(onda_entera1)
voltajes2 = np.array(onda_entera2)
voltajes3 = np.array(onda_entera3)

datos = {'numero_de_item': range(1, 1001), 'MagV1': voltajes1, 'MagV2': voltajes2, 'MagV3': voltajes3}

df = pd.DataFrame(data=datos)
df.to_excel('data.ods', index=False)
