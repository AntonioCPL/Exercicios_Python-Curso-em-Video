t = ("Calculador de Hipotenusa")
print('{:-^40}' .format(t))

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input("Agora digite o valor do cateto adjacente: "))
print('Sabendo que a soma dos catetos ao quadrado é igual a hipotenusa ao quadrado,\no valor da hipotenusa é {:.2f}' .format((co**2+ca**2)**(1/2)))