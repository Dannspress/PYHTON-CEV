Nome = input('Boas-vindas caro construtor. Como você se chama? ')
print('Prazer em te conhecer, {}!'.format(Nome))

h = float(input('Me diga, qual a altura da parede (em METROS)? '))
l = float(input('E a largura? '))

A = h * l
L = A / 2

print('Você quer pintar uma área de: {} m²'.format(A))
print('Para isso, você precisa de {:.1f} Litros de tinta!'.format(L))
