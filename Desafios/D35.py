from datetime import date
Aluno = str(input('Olá! Qual é o seu nome? '))
print('Olá, {}! Vamos definir sua categoria: '.format(Aluno))
ano = int(input('Em que ano você nasceu? '))

hoje = date.today()
idade = -1 * (ano - hoje.year)
print('--' * 20)

if idade <= 9:
    print('Sua categoria é: MIRIM')
elif 10 <= idade <= 14:
    print('Sua categoria é: INFANTIL')
elif 15 <= idade <= 19:
    print('Sua categoria é: JUNIOR')
elif 20 == idade:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')
