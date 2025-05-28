from time import sleep
import os
def pergunta():
    questao = input('Você deseja reiniciar o código? (s/n): ').strip().lower()
    if questao not in ['s', 'n']:
        print('Digite um valor válido')
        sleep(2)
        print('Reinciciando...')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        if questao == 's':
            sleep(1/60)
            print('Reinciando...')
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        else:
            sleep(1/60)
            print('Encerrando...')
            return False
t = 'Conversor de Base Numérica'
print('{:-^42}' .format(t))

while True:
    print()
    print('¨¨'*24)
    print('[1] Para BINÁRIO|[2] Para OCTAL|[3] Para HEXADECIMAL')
    print('¨¨'*24)

    num = input('Digite o número: ').strip()
    base = input('Agora digite a base para a conversão: ').strip()
    try:
        num = int(num)
    except:
        print('Digite um valor válido.')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    if base not in ['1', '2', '3']:
        sleep(1/60)
        print('Digite um valor válido. (1, 2, 3)')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        if base == '1':
            print('O número convertido para binário fica: {:b}.' .format(num))
        elif base == '2':
            print('O número convertido para octal fica: {:o}.' .format(num))
        else:
            print('O número convertido para hexadecimal fica: {:X}.' .format(num))
    if not pergunta():
        break