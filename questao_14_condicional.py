def Idade(i):
    x = 2017 - i
    if x >= 18:
        return "Pode votar"
    else:
        return "Não pode votar"
i = int(input("Digite seu ano de nascimento:"))
print(Idade(i))