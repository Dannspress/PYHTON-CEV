Nome = input('Olá! Qual é o seu nome? ')
print('Boas-vindas {}!'.format(Nome))

C1 = int(input('Por favor, diga um comprimento: '))
C2 = int(input('E diga um segundo comprimento: '))
C3 = int(input('Enfim, diga um terceiro comprimento: '))

print('{:=^25}'.format(''))
print('O 1°Comprimento = {}'.format(C1))
print('O 2°Comprimento = {}'.format(C2))
print('O 3°Comprimento = {}'.format(C3))
print('{:=^25}'.format(''))

AB = C1 + C2
BC = C2 + C3
CA = C1 + C3

if (AB > C3) & (BC > C1) & (CA > C2):
    print('É possível formar um triângulo!')
    print('--' * 20)
    if C1 == C2 and C3 != C1:
        print('O triângulo é ISÓCELES')
    elif C2 == C3 and C3 != C1:
        print('O triângulo é ISÓCELES')
    elif C1 == C3 and C2 != C3:
        print('O triângulo é ISÓCELES')
    elif C3 == C2 and C2 == C1:
        print('O triângulo é EQUILÁTERO')
    else:
        print('O triângulo é ESCALENO')
else:
    print('NÃO É possível formar um triângulo!')