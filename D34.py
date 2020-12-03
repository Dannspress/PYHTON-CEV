Aluno = str(input('Olá! Qual é o seu nome? '))
N1 = float(input('Olá, {}! Qual foi sua primeira nota? '.format(Aluno)))
N2 = float(input('E qual foi sua segunda nota? '))

m = (N1 + N2) /2
print('--' * 20)
print('Sua primeira nota: {}'.format(N1))
print('Sua segunda nota: {}'.format(N2))
print('--' * 20)

if m < 5:
    print('Você foi REPROVADO! (m = {})'.format(m))
elif m >= 7:
    print('Você foi APROVADO! (m = {})'.format(m))
else:
    print('Você ficou de RECUPERAÇÃO! (m = {})'.format(m))