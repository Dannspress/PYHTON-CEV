Nome = input('Olá! Como você se chama, caro amigo? ')
valor = float(input('Ok! Boas-vindas {}! Qual o valor de sua compra? R$ '.format(Nome)))

desc = valor * 0.95

print('Com o desconto, o valor da compra ficou : R$ {}'.format(desc))