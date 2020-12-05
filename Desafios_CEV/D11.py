from math import sqrt, pow
Nome = input('Como você se chama, estudante? ')
print('Prazer em te conhecer, {}!'.format(Nome))

CO = float(input('Por favor, digite o valor do Cateto Oposto: '))
CA = float(input('Obrigado!Agora, digite o valor do Cateto Adjacente: '))
H = sqrt(pow(CO, 2) + pow(CA, 2))
# ou H = hypo(CO, CA)

print('{:=^20}'.format(''))
print('O valor da Hipotenusa é: {:.2f}'.format(H))