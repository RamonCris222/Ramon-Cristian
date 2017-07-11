def Sair(n):
    if n > 20:
        return "Vá ao cinema"
    else:
        return "Fique vendo TV"
n = float(input("Digite um valor real (R$):"))
print(Sair(n))