Nome = input('Olá! Como você se chama? ').upper()
print('Prazer, {}!'.format(Nome))
print('Por favor, nos dê dois valores!')

N1 = int(input('Primeiro Valor: '))
N2 = int(input('Segundo Valor: '))

print('O que deseja fazer? ')
print('-==-' * 20)
print('1 - SOMAR')
print('2 - MULTIPLICAR')
print('3 - VER MAIOR')
print('4 - MUDAR VALORES')
print('5 - SAIR')
menu = int(input('Opção: '))
print('-==-' * 20)

while menu != 5:
    if menu == 1:
        Soma = N1 + N2
        print("A Soma é: {}".format(Soma))

    elif menu == 2:
        Mult = N1 * N2
        print("O produto é: {}".format(Mult))

    elif menu == 3:
        Maior = 0
        if N2 > N1:
            Maior = N2
        elif N1 > N2:
            Maior = N1
        elif N1 == N2:
            Maior = N1
        print("O maior número é: {}".format(Maior))

    elif menu == 4:
        print('Por favor, nos dê dois valores!')

        N1 = int(input('Primeiro Valor: '))
        N2 = int(input('Segundo Valor: '))

    print('----' * 20)
    print('O que deseja fazer? ')
    print('-==-' * 20)
    print('1 - SOMAR')
    print('2 - MULTIPLICAR')
    print('3 - VER MAIOR')
    print('4 - MUDAR VALORES')
    print('5 - SAIR')
    menu = int(input('Opção: '))
    print('-==-' * 20)
