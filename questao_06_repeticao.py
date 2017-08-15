username = input("Forneça um nome de usuário e a sua respectiva senha (não podem ser iguais):\nUsername: ")
password = input("Password: ")

while username == password:

	username = input("Erro: os valores não podem ser iguais.\nUsername: ")
	password = input("Password: ")