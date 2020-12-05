gasto = 0.00
mil = 0
prebar = 100000000000000

while True:
    print('--'*20)
    nome = str(input('PRODUTO: '))
    valor = float(input('PREÇO: R$ '))
    op = str(input('Quer continuar [S/N]? ').upper())

    gasto += valor
    if valor < prebar:
        barato = nome

    if valor > 1000:
        mil += 1

    if op == 'N':
        print('=='*20)
        print(f'Gasto total: R${gasto}')
        print(f'Quantos produtos acima de R$ 1000,00:  {mil}')
        print(f'O produto mais barato: {barato}')
        break
