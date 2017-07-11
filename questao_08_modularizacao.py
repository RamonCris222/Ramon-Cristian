"""Recebe 2 números inteiros, retorne o quociente e o resto da divisão do 1º pelo 2º. Recebe um número inteiro e imprima de volta na tela. """

try:
    def receber(num1 , num2):
        q = (num1 / num2)
        x = num1 % num2
        return q,x
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    q,x = receber(num1 , num2)
    print("O quociente dos números lidos é:", q, "e o resto da divisão dos números lidos é", x)

except:
    print("Você digitou algo errado!")