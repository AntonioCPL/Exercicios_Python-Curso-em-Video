from datetime import date
t = 'Alistamento Militar'
print('{:-^37}' .format(t))

a = input('Você é homem? (s/n) ').strip().lower()
if a not in ['s', 'n']:
    print('Digite um valor válido.')
else:
    if a == 'n':
        print('Beleza, você não precisa se alistar.')
    else:
        n = input('Digite o ano que você nasceu: ').strip()
        try:
            n = int(n)
        except ValueError:
            print('Digite um valor inteiro.')
            quit()
        if date.today().year - n > 18:
            print('Já passou da hora de você se alistar.\nSe passaram {} anos do prazo.' .format((date.today().year - n) - 18))
        elif date.today().year - n < 18:
            print('Ainda não está na hora de você se alistar.\nFaltam {} anos para você se alistar.' .format(18 - (date.today().year - n)))
        elif date.today().year - n == 18:
            print('Está na hora de se alistar.')