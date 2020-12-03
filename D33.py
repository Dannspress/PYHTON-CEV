from datetime import date
Nome = str(input('Olá! Como você se chama? '))
Ano = int(input('Prazer, {}! Em que ano você nasceu? '.format(Nome)))
Hoje = date.today()
Anos = Hoje.year - Ano
if Anos < 18:
    print('Parece que falta algum tempo até seu alistamento.')
elif Anos == 18:
    print('Parece que é tempo de se alistar! Vamos lá soldado!')
else:
    Atrasado = -1 *(18 - Anos)
    print('Ei! Você está com {}! Está {} ANOS atrasado para o alistamento!'.format(Anos, Atrasado))