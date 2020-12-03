Nome = input('Olá! Como você se chama? ')
n = input('Por favor, {}, você poderia digitar um número entre 0 e 9999? '.format(Nome))

print('{:=^25}'.format(''))
print('Número escolhido: {}'.format(n))
print('Milhares: {}'.format(n[0]))
print('Centenas: {}'.format(n[1]))
print('Dezenas: {:>2}'.format(n[2]))
print('Unidades: {}'.format(n[3]))