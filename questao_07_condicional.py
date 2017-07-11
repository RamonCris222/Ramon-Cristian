def SrOuSra(n,s):
    if s == "F":
        return "Ilma Sra."
    else:
        return "Ilmo Sr."
n = input("Digite seu nome:")
s = input("Sexo (M ou F):")
print(SrOuSra(n,s))