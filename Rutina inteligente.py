nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en metros? (ej: 1.65) "))
calorias = []

for dia in range(1, 6):
    valor = int(input(f"Ingrese las calorías del día {dia}: "))
    calorias.append(valor)

rutina = input("¿Cumpliste la rutina? (si/no): ").lower()

rutina = input("¿Cumpliste la rutina? (si/no): ").lower()
if rutina == "si":
    rutina_completada= True
else:
    rutina_completada= False
# promedio de calorías
promedio_calorias = sum(calorias) / len(calorias)

# diferencia entre el valor más alto y más bajo
diferencia_max_min = max(calorias) - min(calorias)

# multiplicar altura por edad (ejercicio simple de tipos)
altura_x_edad = altura * edad

# mensaje personalizado según si completó la rutina
if rutina_completada==True:
    mensaje = f"¡Bien, {nombre}! Rutina completada ✅"
else:
    mensaje = f"Ánimo, {nombre}. Mañana lo intentas de nuevo 💪"

#mostrar resultados
print("nombre:", nombre, "| tipo:", type(nombre))
print("edad:", edad, "| tipo:", type(edad))
print("altura:", altura, "| tipo:", type(altura))
print("\n--- Resultados ---")
print("Calorías por día:", calorias)
print("Promedio calorías:", promedio_calorias)
print("Diferencia (máx - mín):", diferencia_max_min)
print("Altura x edad:", altura_x_edad)
print("Estado:", mensaje)