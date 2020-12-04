Nome = input('Boas-Vindas! Como você se chama? ')
print('Prazer em te conhecer {}!'.format(Nome))

print('{:=^20}'.format(''))
print('Em maiúsculas: {}'.format(Nome.upper()))
print('Em minúsculas: {}'.format(Nome.lower()))
print('A quantidade de letras: {}'.format(len(Nome) - Nome.count(' ')))

NomeD = Nome.split()
print('Seu primeiro nome tem {} letras'.format(len(NomeD[0])))