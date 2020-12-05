Aluno = input('Olá, caro estudante. Como você se chama? ')
print('Um prazer falar com você {}!'.format(Aluno))
Nota1 = float(input('Vamos ao que interessa! Quanto você tirou em sua 1°Nota? '))
Nota2 = float(input('E quanto você tirou em sua 2°Nota? '))

med = (Nota1+Nota2)/2
print('Suas notas foram: {} e {}'.format(Nota1, Nota2))
print('{:=^30}'.format(''))
print('Aqui está a sua média: {:.1f}'.format(med))
print('{:=^30}'.format(''))
print('Obrigado por participar. Volte sempre!')
