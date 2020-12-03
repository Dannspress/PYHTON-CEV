Nome = input('Olá! Qual é o seu nome? ')
print('Boas-vindas {}!'.format(Nome))

N1 = int(input('Por favor, diga um número: '))
N2 = int(input('E diga um segundo número: '))
N3 = int(input('Enfim, diga um terceiro número: '))

print('{:=^25}'.format(''))
print('O 1°N = {}'.format(N1))
print('O 2°N = {}'.format(N2))
print('O 3°N = {}'.format(N3))
print('{:=^25}'.format(''))

# Maior = N1
if N1 > N2 & N2 > N3:
    print ('O maior número é: {}'.format(N1))
    print ('O menor número é: {}'.format(N3))
else:
    if N1 > N2 & N3 > N2:
        print('O maior número é: {}'.format(N1))
        print('O menor número é: {}'.format(N2))
    else: # Maior = N2
        if N2 > N1 & N1 > N3:
            print('O maior número é: {}'.format(N2))
            print('O menor número é: {}'.format(N3))
        else:
            if N2 > N1 & N3 > N1:
                print('O maior número é: {}'.format(N2))
                print('O menor número é: {}'.format(N1))
            else: # Maior = N3
                if N3 > N1 & N1 > N2:
                    print('O maior número é: {}'.format(N3))
                    print('O menor número é: {}'.format(N2))
                else:
                    print('O maior número é: {}'.format(N3))
                    print('O menor número é: {}'.format(N1))
