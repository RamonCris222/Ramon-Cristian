sal = float(input("Digite o valor do salário:"))
perc = float(input("Digite o percentual de aumento:"))

aumento = sal*(perc/100)
novosal = sal + aumento
print("O valor do novo salário será:", novosal)