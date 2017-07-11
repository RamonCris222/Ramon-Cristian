"""Recebe uma velocidade em km/h, retorne esta velocidade em m/s. (Vm/s = Vkm/h / 3.6) """

try:
    def velocidade(vel):
        x = vel // 3.6
        return x
    vel = float(input("Digite a velocidade em quilometros:"))
    x = velocidade(vel)
    print("O equivalente em m/s da velocidade", vel, "é igual a:", x)

except:
    print("Você digitou algo errado!")