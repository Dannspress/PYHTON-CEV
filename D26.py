Nome = input('Olá! Qual é o seu nome? ')
print('Boas-vindas {}!'.format(Nome))

ano = int(input('Por favor, diga um ano: '))

print('{:-^20}'.format(''))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} É Bissexto!'.format(ano))
        else:
            print('O ano {} NÃO É Bissexto!'.format(ano))
    else:
        print('O ano {} É Bissexto!'.format(ano))
else:
    print('O ano {} NÃO É Bissexto!'.format(ano))