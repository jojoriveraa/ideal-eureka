import numpy as np
import pandas as pd

datos_pasajeros = np.loadtxt("TitanicEdades.csv", delimiter=',', dtype='str', unpack=True)
sexo_pasajeros = pd.Series(datos_pasajeros[1], index=datos_pasajeros[0])
edades_pasajeros = pd.Series(datos_pasajeros[2], index=datos_pasajeros[0], dtype=float)

ninos = edades_pasajeros[(edades_pasajeros > 0) & (edades_pasajeros <= 11)]
sexo_ninos = pd.Series(sexo_pasajeros[list(ninos.index)].values, index=ninos.index)

adolescentes = edades_pasajeros[(edades_pasajeros >= 12) & (edades_pasajeros <= 17)]
sexo_adolescentes = pd.Series(sexo_pasajeros[list(adolescentes.index)].values, index=adolescentes.index)

adultos = edades_pasajeros[(edades_pasajeros >= 18) & (edades_pasajeros <= 65)]
sexo_adultos = pd.Series(sexo_pasajeros[list(adultos.index)].values, index=adultos.index)

ad_mayores = edades_pasajeros[edades_pasajeros >= 66]
sexo_ad_mayores = pd.Series(sexo_pasajeros[list(ad_mayores.index)].values, index=ad_mayores.index)

porcentaje_hombres = (sexo_pasajeros[sexo_pasajeros == "HOMBRE"].size / sexo_pasajeros.size) * 100
porcentaje_mujeres = (sexo_pasajeros[sexo_pasajeros == "MUJER"].size / sexo_pasajeros.size) * 100

edades_validas = edades_pasajeros[edades_pasajeros > 0]
menor = edades_validas.min()
mayor = edades_validas.max()
avg_edad = edades_validas.sum() / edades_validas.size

bebes = edades_validas[edades_validas == menor]
abues = edades_validas[edades_validas == mayor]

genero_bebes = sexo_pasajeros[bebes.index]
genero_abues = sexo_pasajeros[abues.index]
