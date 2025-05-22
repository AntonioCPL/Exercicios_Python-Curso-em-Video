import os
import time
def pergunta():
    time.sleep(1)
    b = input('Deseja repetir o código? (s/n) ').strip().lower()
    if b == 's':
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        return False
        
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
            else:
                print('Sim, é bissexto.')
        else:
            print('Sim, é bissexto')
    else:
        print('Não, não é bissexto.')
    if not pergunta():
        break