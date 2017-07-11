"""Recebe uma velocidade em m/s, retorne esta velocidade em km/h. (Vkm/h = Vm/s * 3.6) """

try:
    def velocidade(vel):
        x = vel*3.6
        return x
    vel = float(input("Digite a velocidade em metros:"))
    x = velocidade(vel)
    print("O equivalente em km/h da velocidade", vel, "é igual a:", x)

except:
    print("Você digitou algo errado!")