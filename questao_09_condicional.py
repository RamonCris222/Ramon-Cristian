def MultiploDeCinco(n):
    if n % 5 == 0:
        return "Verdadeiro"
    else:
        return "Falso"
n = int(input("Digite um numero:"))
print(MultiploDeCinco(n))