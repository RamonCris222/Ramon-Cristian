def Multiplo(n):
    if n % 7 == 0:
        return "O numero e multiplo de 7"
    else:
        return "O numero não e multiplo de 7"
n = int(input("Digite um numero:"))
print(Multiplo(n))