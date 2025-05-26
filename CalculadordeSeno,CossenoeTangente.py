from math import sin, cos, tan, radians

t = ('Calculador de Seno, Cosseno e Tangente')
print('{:-^54}' .format(t))

a = float(input('Digite um ângulo: '))
print('O valor do seno desse ângulo é {:.2f},\n do cosseno é {:.2f}\n e da tangente é {:.2f}.' .format(sin(radians(a)), cos(radians(a)), tan(radians(a))))