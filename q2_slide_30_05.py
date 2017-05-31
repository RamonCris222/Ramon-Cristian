try:

    val = float(input("Digite o valor em real:"))

    calculo = val * (70 / 100)
    print("O valor de", val, "com 70% é igual a:", calculo)

except:
    print("Você digitou um valor errado!!")