t = 'Calculador de Frequência de Caracteres'
print('{:-^54}' .format(t))

n = input('Digite uma frase: ').lower().strip()
n = n.replace('ã', 'a')
n = n.replace('â', 'a')
n = n.replace('á', 'a')
n = n.replace('ê', 'e')
n = n.replace('í', 'i')
n = n.replace('õ', 'o')
n = n.replace('ô', 'o')
contador = {}
letras = ''
for caractere in n:
    if caractere.isalpha() or caractere.isdigit():
        if caractere not in letras:
            letras += caractere
            contador[caractere] = 1
        else:
            contador[caractere] += 1
for letra, contagem in contador.items():
    print('A letra {} aparece {} vez(es).' .format(letra, contagem))