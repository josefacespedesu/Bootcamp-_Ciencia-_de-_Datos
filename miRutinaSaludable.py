peso= float(input("Ingresa tu peso en kg (ej. 75): "))
altura= float(input("Ingresa su altura en metros (ej. 1.63): "))

#calcula imc
def calcular_imc (peso,altura):
    return round(peso/(altura**2),2)

#clasifica el imc
def clasificar_imc (imc):
    if imc<18.5:
        return "bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

#calcula y categoriza
valor_imc = calcular_imc(peso, altura)
categoria = clasificar_imc(valor_imc)

print (valor_imc, categoria)
