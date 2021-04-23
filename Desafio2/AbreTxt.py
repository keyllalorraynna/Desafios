#Programa que irá abrir o arquivo txt versao 123456789

print("Esses são os nomes do arquivo, com seus respectivos ID's.")

arq = open("Nomes.txt")
agora_vai = arq.read()

for imprimir in agora_vai:
	print(imprimir)