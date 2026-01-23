import numpy as np
np.random.seed(42)

#Simular una matriz 5x7 con temperaturas aleatorias entre 10°C y 40°C

X = np.random.randint(10, 41, size=(5, 7))

print(f"Matriz temperaturas :\n {X}")

#Identificar las temperaturas que superan los 30°C
mayores_30 = X[X > 30]
print(f"Temperaturas mayores a 30 :\n {mayores_30}")

#Reemplazar los valores inferiores a 15°C por el valor 15
X_nueva=X.copy ()
X_nueva[X_nueva < 15] = 15
print(f"Nueva matriz de temperaturas :\n {X_nueva}")
# en este caso también peude ser así X_nueva = np.where(X < 15, 15, X)

#Calcular la media de temperaturas por ciudad (por fila) y por día (por columna)
media_ciudad = X.mean(axis=1)
print(f"Media temperaturas por ciudad (fila) :\n {media_ciudad}")

media_dia = X.mean(axis=0)
print(f"Media temperaturas por día (columna) :\n {media_dia}")

#Determinar cuál es la ciudad con la mayor temperatura promedio
indice_ciudad = np.argmax(media_ciudad)
print(f"\nCiudad con mayor promedio: Ciudad {indice_ciudad + 1} "
      f"({media_ciudad[indice_ciudad]:.2f}°C)") #:.2f significa float con 2 decimales
