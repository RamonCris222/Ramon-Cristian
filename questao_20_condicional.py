def Imc(m,h):
    i = m / (h ** 2)
    if i < 18.5:
        return "Abaixo	do	peso"
    elif i < 25:
        return "Peso normal"
    elif i < 30:
        return "Sobrepeso"
    elif i < 35:
        return "Obeso leve"
    elif i < 40 :
        return "Obeso moderado"
    elif i >= 40:
        return "Obeso mórbido"
m = float(input("Digite seu peso:"))
h = float(input("Digite sua altura:"))
print(Imc(m,h))