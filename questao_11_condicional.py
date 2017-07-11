def Febre(t):
    if t > 36.5:
        return "Está com febre"
    else:
        return "Sem febre"
t = float(input("Digite sua temperatura:"))
print(Febre(t))