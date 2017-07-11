"""Recebe quatro números e imprima a média ponderada, sabendo-se que os pesos são respectivamente 1, 2, 3 e 4. """

try:
    def mediapon(num1 , num2 , num3 , num4):
        a = ((num1 * 1) + (num2 * 2) + (num3 * 3) + (num4 * 4))/10
        return a
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    num3 = float(input("Digite o terceiro número:"))
    num4 = float(input("Digite o quarto número:"))
    a = mediapon(num1 , num2 , num3 , num4)
    print("A média ponderada dos números lidos é:", a)
except:
    print("Você digitou algo errado!")