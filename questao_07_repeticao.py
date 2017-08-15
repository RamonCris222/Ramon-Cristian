try:

	b = int(input("Forneça dois valores inteiros para 'b' e 'n', respectivamente (com b >= 2 e n > 1): "))
	n = int(input())

	while b < 2 or n <= 1:

		try:

			b = int(input("Forneça dois valores inteiros para 'b' e 'n', respectivamente (com b >= 2 e n > 1): "))
			n = int(input())

		except:

			print("Não foram fornecidos valores inteiros.")

	print("'b' elevado a 'n' é %d." % pow(b, n))

except:

	print("Não foram fornecidos valores inteiros.")