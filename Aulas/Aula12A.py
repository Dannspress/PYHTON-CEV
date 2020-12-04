Nome = str(input('Olá! Como você se chama? '))
Nome = Nome.capitalize()

print('==' * 10)
if Nome == 'Dan':
    print('{}?! Não é você o namorado da Andressa?'.format(Nome))
elif Nome == 'Andressa' or Nome == 'Adrien':
    print('Olá, {}! Como está seu namorado? '.format(Nome))
else:
    print('Ah...olá, {}.'.format(Nome))
