def SinalDeTransito(x):
    if x == "v":
        return "Siga"
    elif x == "a":
        return "Atenção"
    elif x == "e":
        return "Pare"
x = input("Digite a cor do sinal de transito(v, a ou e):")
print(SinalDeTransito(x))