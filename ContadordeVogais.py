t = 'Contador de Vogais'
print('{:-^34}' .format(t))

n = input('Digite uma frase: ')
contador = 0
for vogal in n.lower():
 if vogal in 'aeiou':
  contador += 1
print('A quantidade de vogal(is) nesta frase é de: {}.' .format(contador))