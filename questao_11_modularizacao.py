"""Recebe nome, endereço e telefone e imprima na tela. """

try:
    def lista(nome , endereco , telefone):
        x = nome
        y = endereco
        z = telefone
        return x,y,z
    nome = input("Digite um nome:")
    endereco = input("Digite o endereço:")
    telefone = int(input("Digite um telefone:"))
    x,y,z = lista(nome , endereco, telefone)
    print("O nome", nome,"tem como endereço", endereco, "e como telefone", telefone)

except:
    print("Você digitou algo errado!")