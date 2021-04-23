#Desafio 6
import csv

with open("dados.csv", 'r', newline='') as arq:

    '''ler1 = csv.reader(arq, delimiter=',')
    for nav in ler1:
        id_num = nav[0]
        nome = nav[1]
        salario = nav[2]
        print(id_num, nome, salario)'''
        
    ler1 = csv.reader(arq)
    ler1.writerow(["id", "nome", "salario"])
	ler1.writerow(["1", "fulano", "1000.00"])
	ler1.writerow(["2", "beltrano", "2000.00"])
	ler1.writerow(["3", "andre", "1500.00"])
	ler1.writerow(["4", "renato", "10.50"])