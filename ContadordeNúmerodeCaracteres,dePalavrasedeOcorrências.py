from collections import Counter
t = 'Contador de Caracteres, Total de Palavras e de Ocorrências'
print('{:-^74}' .format(t))
n = input('Digite uma frase: ')
comprimento = len(n.lower().strip())
ocorrências = Counter(n.title().split())
palavras = len(n.lower().split())
print('A quantidade de caracteres dessa frase é de: {}. \nA quantitade de palavras é de: {}. \nE a quantidade de ocorrências, ou seja, a repetição de cada palavra é de: {}.' .format(comprimento, palavras, ocorrências))