Nome = input('Boas-vindas viajante! Como você se chama? ')
n = int(input('É um prazer te conhecer {}! Por favor, digite um número: '.format(Nome)))
ante = n-1
suce = n+1

print('Você escolheu o número: {}'.format(n))
print('{:=^30}'.format(''))
print('Seu antecessor é o número: {}'.format(ante))
print('E seu sucessor é o número: {}'.format(suce))
print('{:=^30}'.format(''))
print('Obrigado por participar. Volte sempre!')