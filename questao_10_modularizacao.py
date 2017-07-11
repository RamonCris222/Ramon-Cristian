"""Escreva um algoritmo/programa que mostre o triplo de um número informados pelo usuário."""

try:
    def triplo(num):
        x = num * 3
        return x
    num = int(input("Digite um número:"))
    x = triplo(num)
    print("O triplo de", num, "é:", x)

except:
    print("Você digitou algo errado!")