valor = float(input("Digite o valor do produto em atraso:"))
taxa = float(input("Digite o valor da taxa do produto em atraso:"))
tempo = float(input("Digite o tempo de atraso:"))

prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor da prestação em atraso é:", prestacao)