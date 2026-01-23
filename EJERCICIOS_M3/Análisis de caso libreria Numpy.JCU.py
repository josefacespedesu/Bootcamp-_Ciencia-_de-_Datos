import numpy as np

# Creamos una semilla para que los datos sean los mismos
np.random.seed(42)
#1.Carga y estructuración de datos 
# Creamos una matriz 5x5 con precios simulados entre 100 y 200->filas:acciones, columnas:días de cotización
precios = np.random.uniform(100, 200, size=(5, 5))

print(f"Matriz de precios (acciones x días): \n{precios}")

#2.Análisis y transformación de datos
#promedio, valor máximo y mínimo de cada acción a lo largo del tiempo
promedio = np.mean(precios, axis=1)
maximo = np.max(precios, axis=1)
minimo = np.min(precios, axis=1)

print(f"\nPromedio por acción: {promedio}\nMáximo por acción:{maximo} \nMínimo por acción: {minimo}")

#variación porcentual diaria de cada acción ((precio dia actual-precio día anterior)/(precio día anterior))*100
#precios[:, :-1] se usa para ajustar de la matriz original para que coincida con el resultado
variacion_diaria = np.diff(precios, axis=1) / precios[:, :-1] * 100

print(f"\nVariación porcentual diaria:\n{variacion_diaria}")

#Aplica funciones matemáticas como logaritmo, exponencial o normalización sobre los datos
#Logaritmo
log_precios = np.log(precios)
print("\nPrecios con logaritmo:")
print(log_precios)
# Exponencial
exp_precios = np.exp(precios/100)  # se divide para evitar números muy grandes
print("\nPrecios Exponencial (dividido en 10 para números más pequeños):")
print(exp_precios)
# Normalización (valores entre 0 y 1)
normalizados = (precios - precios.min()) / (precios.max() - precios.min())
print("\nPrecios normalizados:")
print(normalizados)

#3.Optimización y selección de datos
#Utiliza indexación avanzada para extraer información especíﬁca
accion = 2  # tercera acción porque parten en índice 0
dia = 3     # cuarto día

print(f"\nPrecio de la acción {accion + 1} en el día {dia + 1}:",
      precios[accion, dia])

#Aplica broadcasting para realizar operaciones sin necesidad de bucles
#Cada día se aplica un ajuste porcentual
ajuste_porcentual_diario = np.array([1.00, 1.01, 0.99, 1.02, 1.03])

#se multiplica la matriz original pot el vector de los ajustes porcentuales
precios_ajustados = precios * ajuste_porcentual_diario
print("\nBroadcasting, se multiplica la matriz original por un vector de ajuste porcentual diario, dando una nueva matriz con ajuste porcentual diario (el día 1 se mantiene el porcentaje original)")
print("\n", precios_ajustados)

#4.Comparación con otros métodos
#Matriz ejemplo
precios_lista = [
    [120, 130, 125, 140, 150],
    [100, 110, 105, 115, 120],
    [200, 195, 198, 202, 205],
    [90, 95, 100, 98, 102],
    [160, 158, 162, 165, 170]
]

print(f"\nMatriz ejemplo parte 4, realizada como lista. \n{precios_lista}")
#SIN NUMPY, SACO PROMEDIO DE PRECIOS
promedios = []
for accion in precios_lista:
    promedios.append(sum(accion) / len(accion))

print("\nPromedios sin NumPy: Debe crearse un for para ir agregando los datos y calcular el promedio. Resultado", promedios)

#EJEMPLO CON NUMPY
print("\nPromedios con NumPy: Se realiza en menos de una línea de código teniendo la matriz de ejemplo, usando np.mean. Dando el mismo resultado", np.mean(precios_lista, axis=1))