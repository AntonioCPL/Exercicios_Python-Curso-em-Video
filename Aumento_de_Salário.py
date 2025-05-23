import os
import time
def escolha(a, n):
    if a == '%':
        b = input('Digite a porcentagem do aumento de seu salário: ').strip()
        try:
            b = float(b)
        except ValueError:
            print('Digite de acordo com as regras.')
            time.sleep(1.5)
            print('Reiniciando...')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        print('A soma do seu salário atual com {:.2f}% de aumento fica: R${:.2f}.' .format(b, n + n *(b/100)))
    elif a != 'r$':
        print('Digite de acordo com as regras.')
        time.sleep(1.5)
        print('Reinciando...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        b = input('Digite o valor do seu aumento para converte-lo em porcentagem: R$').strip()
        try:
            b = float(b)
        except ValueError:
            print('Digite de acordo com as regras.')
            time.sleep(1.5)
            print('Reiniciando...')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        print('A porcentagem do aumento do seu salário com R${} é de: {:.0f}%.' .format(b, (b*100) /n))
    c = input('Deseja reiniciar o código? (s/n): ').strip().lower()
    if c not in ['s', 'n']:
        print('Digite de acordo com as regras.')
        time.sleep(1.5)
        print('Reinciando...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    if c == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        return False
    
t = 'Aumento de Salário'
print('{:-^34}' .format(t))

while True:
    n = input('Digite o seu salário atual: R$').strip()
    try:
        n = float(n)
    except ValueError:
        print('Digite de acordo com as regras.')
        time.sleep(1.5)
        print('Reiniciando...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    a = input('Agora digite se você quer digitar a porcentagem do aumento de seu salário, ou o valor do aumento para ver a porcentagem (%/R$): ').strip().lower()
    if a not in ['%', 'r$']:
        print('Digite de acordo com as regras.')
        time.sleep(1.5)
        print('Reiniciando...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    if not escolha(a, n):
        break
