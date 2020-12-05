Nome = input('Olá! Como você se chama? ')
print('Prazer em te conhecer, {}!'.format(Nome))

num = int(input('Digite um número! Por favor: '))

if num % 2 == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))