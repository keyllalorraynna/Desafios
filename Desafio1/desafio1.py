try:
	''' Cliente insere os valores'''
	ganho_por_hora = float(input("Quanto você ganha por hora? "))
	horas_por_dia = int(input("Quantas horas você trabalha por dia? "))

	'''Salário bruto'''
	salario_bruto = ganho_por_hora * horas_por_dia

	'''Imposto de renda'''
	imposto_de_renda = 11 / 100 * salario_bruto

	'''INSS''' 
	inss = 8/100 * salario_bruto

	'''Sindicato'''
	sindicato = 5/100 * salario_bruto

	'''Salário Liquido'''
	salario_liq = (((salario_bruto - imposto_de_renda) - inss) - sindicato)

	print (f' + Salário bruto: R$ {salario_bruto}. ')
	print (f' - IR (11%): R$ {imposto_de_renda}. ')
	print (f' - INSS (8%): R$ {inss}. ')
	print (f' - Sindicato (5%): R$ {sindicato}. ')
	print (f' = Salario liquido: R$ {salario_liq}. ')
except ValueError:
	print ('Por favor, insira apenas números. E por favor usar "." ao invés de "," .')
