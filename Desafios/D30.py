Nome = str(input('Olá! Como você se chama? '))
valorC = float(input('Prazer, {}! Quanto custa a sua casa? '.format(Nome)))
sal = float(input('Qual o valor do seu salário? '))
anos = int(input('E em quantos anos você pretende pagar? '))

prest = valorC / (12*anos)
lim = sal * 0.30

print('==' * 20)
if prest > lim:
    print('Limite alcançado. ACESSO NEGADO')
else:
    print('{},sua prestação mensal para {} anos será de: R$ {:.2f}'.format(Nome, anos, prest))