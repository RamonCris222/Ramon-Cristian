def sinal(n):
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    else:
        return "zero"
n = int(input("Digite um numero:"))
print(sinal(n))