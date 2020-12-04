from math import floor

Nome = input('Olá! Como você se chama? ')
print('Prazer em te conhecer, {}!'.format(Nome))

n = float(input('Por favor, digite um número do conjuto dos Reais: '))

print('A porção inteira de {} é: {}'.format(n, floor(n)))