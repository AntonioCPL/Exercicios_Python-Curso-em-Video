import os
import time
t = 'Ano Bissexto'
print('{:-^28}' .format(t))

while True:
    n = input('Digite um ano aleatório, que não tenha casas decimais (EX: 3344, 77777): ').strip()
    try:
        a = int(n)
    except ValueError:
        print('Digite de acordo com as Regras.')
        time.sleep(1)
        print('Reiniciando...')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 != 0:
                print('Não, não é bissexto.')
                time.sleep(1)
                b = input('Deseja repetir o código? (s/n) ').strip().lower()
                if b == 's':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                else:
                    quit()
            else:
                print('Sim, é bissexto.')
                time.sleep(1)
                b = input('Deseja repetir o código? (s/n) ').strip().lower()
                if b == 's':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                else:
                    quit()
        else:
            print('Sim, é bissexto')
            time.sleep(1)
            b = input('Desejaria repetir o código? (s/n) ').strip().lower()
            if b == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                quit()
    else:
        print('Não, não é bissexto.')
        time.sleep(1)
        b = input('Deseja repetir o código? (s/n) ').strip().lower()
        if b == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            quit()
