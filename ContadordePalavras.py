t = 'Contador de Palavras'
print('{:-^36}' .format(t))

n = input('Digite uma frase: ')
palavras = n.lower().split()
for palavra in palavras:
    print(palavra)