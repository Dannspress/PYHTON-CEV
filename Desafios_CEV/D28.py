Nome = input('Olá! Qual é o seu nome? ')
print('Prazer em te conhecer cliente {}!'.format(Nome))

sal = float(input('Qual o valor de seu salário? R$ '))
Tsal = 0

if sal > 1250.00:
    Tsal = sal * 1.10
    print('Seu salário com 10% de aumento é: R${:.2f}'.format(Tsal))
else:
    Tsal = sal * 1.15
    print('Seu salário com 15% de aumento é: R${:.2f}'.format(Tsal))
