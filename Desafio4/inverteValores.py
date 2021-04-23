''' Faça um programa que peça um numero inteiro positivo e em seguida mostre este
numero invertido.
•Exemplo:
12376489
=> 98467321 '''

insere_valor = input('Digite os valores que devem ser invertidos: ')

for i in reversed(insere_valor):
	print (f'{i}', end = '')