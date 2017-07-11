"""Recebe um valor em minutos, retorna o equivalente em horas e minutos. QUESTÃO IGUAL A TERCEIRA"""

try:
    def minutos(min):
        x = min // 60
        y = min % 60
        return x,y
    min = int(input("Digite os minutos:"))
    x,y = minutos(min)
    print("O equivalente em horas e minutos de", min, "é igual a:", x,"hora e", y,"minutos")
except:
    print("Você digitou algo errado!")