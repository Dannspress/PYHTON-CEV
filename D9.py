Nome = input('Olá! Como você se chama, caro amigo? ')
valor = float(input('Ok! Boas-vindas {}! Qual o valor do seu salário? R$ '.format(Nome)))

aum = valor * 1.15

print('Com o aumento, o seu salário agora é : R$ {}'.format(aum))