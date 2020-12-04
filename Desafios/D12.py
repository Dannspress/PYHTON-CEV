from math import tan, cos, sin, radians
Nome = input('Olá! Como você se chama? ')
print("Olá, {}!".format(Nome))

Ang = float(input('Por favor, digite o valor do ângulo: '))
T = tan(radians(Ang))
C = cos(radians(Ang))
S = sin(radians(Ang))

print('{:=^20}'.format(''))
print('Seu Seno é: {:.3f}'.format(S))
print('Seu Cosseno é: {:.3f}'.format(C))
print('Sua Tangente é: {:.3f}'.format(T))