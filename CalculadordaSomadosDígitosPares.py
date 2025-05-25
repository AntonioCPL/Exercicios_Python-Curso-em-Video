t = 'Calculador da Soma dos Dígitos Pares'
print('{:-^53}' .format(t))

n = input('Me digite uma frase que contenha dígitos númericos: ')
digitos = 0
for digito in n:
  if digito.isdigit():
    if digito in '2468':
     digitos += int(digito)
print('A soma dos dígitos pares dessa frase é de: {}.' .format(digitos))