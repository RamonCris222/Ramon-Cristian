""" Recebe um valor em real (R$), retorna 70% deste valor.  """
try:
    def valor(num):
        return num*0.7
    x = float(input("Digite o valor: "))
    print("O 70% do valor é", valor(x))

except:
    print("Você digitou algo errado!")