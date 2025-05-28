# importa as bibliotecas necessárias

from time import sleep
import os

# cria a função pergunta
def pergunta():

    # recebe se a pessoa deseja reiniciar o código
    questao = input('Você deseja reiniciar o código? (s/n) ').strip().lower()

    # verifica se a pessoa digitou s ou n e senão manda uma mensagem de erro
    if questao not in ['s', 'n']:
        print('Digite "s" ou "n".'), sleep(1)
        print('Reiniciando...'), sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        # verifica se a pessoa quer reiniciar o código e se quiser reinicia, senão não reinicia
        if questao == 's':
            print('Ótimo.'), sleep(1)
            print('Reiniciando...'), sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        else:
            print('Ok')
            return False

print(f"{'Contagem Regresiva':-^34}")

# inicia o looping caso depois na pergunta a pessoa deseja reiniciar o código

while True:

    # recebe o número que a pessoa digitar
    num = input('Digite um número aleatório que seja inteiro e positivo: ').strip()

    # verifica se esse número é positivo e senão manda uma mensagem de erro
    if '-' in num:
        print('Digite um número positivo'), sleep(1)
        print('Reiniciando...'), sleep(3)
        os.system('cls') if os.name == 'nt' else 'clear'
        continue
    else:
        # verifica se esse número é inteiro e senão manda uma mensagem de erro
        try:
            num = int(num)
        except ValueError:
            print('Digite um número inteiro e positivo'), sleep(1)
            print('Reiniciando...'), sleep(3)
            os.system('cls') if os.name == 'nt' else 'clear'
            continue

    # faz um looping que vai do número que a pessoa digitou até zero, decrescentemente
    for i in range(num, 0, -1):
        print(i)
    print('-FIM-')

    # chama a função pergunta
    if not pergunta():
        break
