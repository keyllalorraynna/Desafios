'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será
digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar
em 10, o valor inicial e final devem ser informados também pelo usuário, conforme
exemplo abaixo:
•Montar a tabuada de: 5
Começar por: 4
Terminar em: 7
Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35 '''

try:
  tabuada = int(input('De qual número será a tabuada? '))
  comeco = int(input('Ela deverá começar por qual número? '))
  fim = int(input('Ela deverá terminar em qual número? '))

  if comeco > fim:
    print('O número de início deve ser maior que o número final!')

  else:  
    while comeco <= fim:
      conta = tabuada * comeco
      print(f'{tabuada} X {comeco} = {conta}')
      comeco = comeco + 1

except (ValueError):
  print('Por favor digitar apenas números inteiros!')
