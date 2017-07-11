"""Recebe um número inteiro e imprima na tela seu antecessor e o seu sucessor. """

try:
    def antesuc(num):
        x = num - 1
        y = num + 1
        return x,y
    num = int(input("Digite um número:"))
    x,y = antesuc(num)
    print("O antecessor de", num, "é", x, "e o seu sucessor é:", y)

except:
    print("Você digitou algo errado!")