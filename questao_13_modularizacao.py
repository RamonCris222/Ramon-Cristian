"""Recebe o ano de nascimento de uma pessoa e escreva na tela a sua idade em 31/12/2013. """

try:
    def idade(nas):
        x = 2013 - nas
        return x
    nas = int(input("Digite o ano de nascimento:"))
    x = idade(nas)
    print("No dia 31/12/2013 a pessoa terá:", x)


except:
    print("Você digitou algo errado!")