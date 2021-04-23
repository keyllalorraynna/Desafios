# inspiradamente em Dolglas
import csv

with open("dados.csv", 'w', newline='') as arq:
	
	escreve = csv.writer(arq)
	escreve.writerow(["id", "nome", "salario"])
	escreve.writerow(["1", "fulano", "1000.00"])
	escreve.writerow(["2", "beltrano", "2000.00"])
	escreve.writerow(["3", "andre", "1500.00"])
	escreve.writerow(["4", "renato", "10.50"])

arq.close()

while True:
	print("1- Listar | 2- Incluir | 3- Excluir")
	escolha = int(input("Escolha uma das opções acima, digitando o respectivo número: "))

	if(escolha == 1):
		with open("dados.csv") as arq:
			listar = csv.reader(arq)

			for linha in listar:
				print (linha)
			print("\n")

	elif(escolha == 2):
		id_num = input("Id: ")
		nome = input("Nome: ")
		salario = input("Salário: ")

		with open("dados.csv", 'a', newline='') as arq:
			incluir = csv.writer(arq)
			incluir.writerow([id_num, nome, salario])
			print("\n")
		arq.close()
		
	elif(escolha == 3):
		with open("dados.csv", 'w', newline='') as arq:
			escreva = csv.writer(arq)
			escreva.writerow(["id", "nome", "salario"])
			print("Todos os dados da tabela foram apagados =D")
			print("\n")
		arq.close()
	else:
		print("Opção inválida")
		print("\n")