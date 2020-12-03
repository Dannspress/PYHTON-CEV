Nome = str(input('Olá! Por favor, diga seu nome: '))

N1 = float(input('Olá, {}! Escolha um número: '.format(Nome)))
N2 = float(input('Um segundo número, por favor: '))

print('1° Número: {}'.format(N1))
print('2° Número: {}'.format(N2))
print('--' * 20)

if N1 > N2:
    print('O maior número é: {}'.format(N1))
elif N2 > N1:
    print('O maior número é: {}'.format(N2))
else:
    print('Não há maior. Os dois números são iguais!')