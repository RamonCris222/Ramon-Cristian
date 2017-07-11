def Par(n):
    if n % 2 == 0:
        return "Verdadeiro"
    else:
        return "Falso"

n = int(input("Digite um numero:"))
print(Par(n))