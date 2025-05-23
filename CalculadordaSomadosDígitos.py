t = 'Calculador da Soma dos Dígitos'
print('{:-^48}' .format(t))

n = input('Me digite uma frase que contenha dígitos númericos: ')
digitos = 0
for digito in n:
  if digito.isdigit():
    digitos += int(digito)
print('A soma dos dígitos dessa frase é de: {}.' .format(digitos))