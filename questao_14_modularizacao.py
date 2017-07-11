"""Recebe um número inteiro de 3 dígitos e mostre na tela o dígito da casa das dezenas. FALTA CORRIGIR """

try:
    def dezenas(num):
            if num == 3:
                centena = num[0:1]
                dezena = num[1:2]
                unidade = num[2,3]
                print (num+ "= +centena+", centena)
            if num == 2:
                dezena = num[0:1]
                unidade = num[1,2]
                print (num+ "= +dezena+", dezena)
            if num == 1:
                unidade = num[0:1]
                print(num + "= +unidade+", unidade)
                return x
    num = int(input("Digite um número de três dígitos:"))
    x = dezenas(num)
    print(num, "O número", , "é da casa das centenas", 2,"casa das dezenas", 1,"casa das unidades" )

except:
    print("Você digitou algo errado!")