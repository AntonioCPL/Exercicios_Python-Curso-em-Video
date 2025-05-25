t = 'Calculador de Palavra Mais Longa'
print('{:-^48}' .format(t))

n = input('Digite uma frase: ').strip()
fraselimpa = ''
for símbolo in n:
    if símbolo.isalnum() or símbolo == ' ':
        fraselimpa += símbolo
maiorpalavra = ''
tamanhomaiorpalavra = 0
for palavra in fraselimpa.split():
    if len(palavra) > tamanhomaiorpalavra:
        maiorpalavra = palavra
        tamanhomaiorpalavra = len(maiorpalavra)
print('A maior palavra é "{}" e o seu tamanho é de {} caracteres.' .format(maiorpalavra, tamanhomaiorpalavra))