nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

# espaço é :
# centralizar é ^ ou < ou >

n1 = int(input('Olá novamente {}! Digite um número, por favor? '.format(nome)))
n2 = int(input('Obrigado! Por favor, um segundo número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma deles vale: {}'.format(s))
print('A multiplicação deles vale: {}'.format(m))
print('A divisão deles vale: {:.3f}'.format(d))
print('A divisão inteira deles vale: {}'.format(di))
print('O primeiro elevado ao segundo vale: {}'.format(e))

# end = ' ' (Juntar print's)
# \n (quebrar linha)