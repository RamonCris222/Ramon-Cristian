"""Recebe 2 números, retorne a divisão da soma pela subtração dos números lidos. 08"""

try:
    def divisao(x, y):
        div = (x + y) / (x - y)
        return div
    x = int(input("Digite o primeiro número:"))
    y = int(input("Digite o segundo número:"))
    div = divisao(x, y)
    print("A divisão da soma pela subtração dos números lidos é:", div)

except:
    print("Você digitou algo errado!")