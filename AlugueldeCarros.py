t = 'Para calcular o Aluguel de um Carro'
print('{:-^51}' .format(t))

dias = int(input('Quantos dias você ficou com o carro? '))
valor = float(input('Agore digite o valor diário dele: R$'))
km = int(input('Quantos quilômetros foram percorridos com o carro? '))
valor2 = float(input('Agora digite o valor de cada quilômetro percorrido: R$'))
soma = (dias * valor) + (km * valor2)
print('Com esses valores, o valor total a pagar é de R${:.2f}.' .format(soma))