def vogal(n):
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        return "verdadeiro"
    else:
        return "falso"
n = input("Digite uma vogal:")
print(vogal(n))