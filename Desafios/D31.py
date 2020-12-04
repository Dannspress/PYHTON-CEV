Nome = str(input('Olá! Como você se chama? '))
num = int(input('Prazer, {}! Escolha um número: '.format(Nome)))
print('---' * 20)
print('Esolha a opção de conversão: ')
print('1 - BINÁRIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
op = int(input('Opção escolhida: '))
print('---' * 20)

if op == 1:
    B = False
    B = bool(num)
    print("O número {} em BINÁRIO é: {}".format(num, B))
elif op == 2:
    O = oct(num)
    print('O número {} em OCTAL é: {}'.format(num, O))
elif op == 3:
    H = hex(num)
    print('O número {} em HEXADECIMAL é: {}'.format(num, H))
else:
    print('OPÇÃO INEXISTENTE')