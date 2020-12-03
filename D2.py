Nome = input('Boas-vindas viajante! Como você se chama? ')
n = int(input('É um prazer te conhecer {}! Por favor, digite um número: '.format(Nome)))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('Você escolheu o número: {}'.format(n))
print('{:=^30}'.format(''))
print('Seu dobro é o número: {}'.format(dobro))
print('Seu triplo é o número: {}'.format(triplo))
print('Sua raiz quadrada é o número: {:.3f}'.format(raiz))
print('{:=^30}'.format(''))
print('Obrigado por participar. Volte sempre!')