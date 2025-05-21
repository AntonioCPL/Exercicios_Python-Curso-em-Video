from random import randint
import os
import time
t = 'Adivinhação Entre 1 e 5'
print('{:-^39}' .format(t))
while True:
    lista = 1
    escolha = randint(1, 5)
    n = ((input('Chute um número de 1 a 5: ')))
    if n.isdigit() == False:
        print('Faça conforme as regras.')
        time.sleep(2)
        print('Reinciciando...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        a = int(n)
    if a > 5 or a < 1:
        print('Faça conforme as regras.')
        time.sleep(2)
        print('Reiniciando...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        while a != escolha:
            while a < escolha:
                a = int(input('É maior: '))
                lista += 1
            while a > escolha:
                    a = int(input('É menor: '))
                    lista += 1
    print('Parabéns, você levou {} tentativa(s).' .format(lista))
    time.sleep(1)
    z = input('Deseja reiniciar? (s/n): ').strip().lower()
    if z not in ['s', 'n']:
         print('Faça conforme as regras.')
         time.sleep(2)
         print('Reiniciando...')
         time.sleep(2)
         os.system('cls' if os.name == 'nt' else 'clear')
         continue
    else:
        if z == 's':
              time.sleep(1/60)
              print('Reiniciando...')
              time.sleep(2)
              os.system('cls' if os.name == 'nt' else 'clear')
        else:
             break