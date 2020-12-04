Nome = str(input('Qual é o seu nome? '))
print('Olá, {}!'.format(Nome))

valor = float(input('Qual é o valor a ser pago? R$ '))
print('Qual o método? ')
print('1 - À vista (dinheiro/cheque)')
print('2 - À vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais')
op = int(input('Opção: '))

print('--' * 20)
if op == 1:
    total = valor * 0.90
    print('Valor a ser pago: R$ {}'.format(total))
elif op == 2:
    total = valor * 0.95
    print('Valor a ser pago: R$ {}'.format(total))
elif op == 3:
    parcela = valor/2
    print('Valor: R$ {}'.format(valor))
    print('Em 2x o valor a ser pago mensalmente é: R$ {:.2f}'.format(parcela))
elif op == 4:
    num = int(input('Em quantas vezes você quer fazer? '))
    if num > 2:
        valor20 = valor * 1.20
        parcela = valor20 / num
        print('--' * 20)
        print('Valor: R$ {}'.format(valor20))
        print('Em {}x o valor a ser pago mensalmente é: R$ {:.2f}'.format(num, parcela))
    else:
        parcela = valor / 2
        print('Valor: R$ {}'.format(valor))
        print('Em 2x o valor a ser pago mensalmente é: R$ {:.2f}'.format(parcela))
else:
    print('OPÇÃO INVÁLIDA')