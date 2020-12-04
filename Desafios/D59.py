print('Bem-vindo(a)!')
n = int(input('Quantos números você deseja? '))
s = 0
i = 1

valor = 0
MAIvalor = 0
menvalor = 0

while i <= n:
    valor = int(input('Qual o {}° valor? '.format(i)))
    if i == 1:
        MAIvalor = valor
        menvalor = valor

    if MAIvalor < valor:
        MAIvalor = valor

    if valor < menvalor < MAIvalor:
        menvalor = valor

    if i == n:
        op = 'x'
        op = str(input('Você quer continuar [S/N]? ').upper())
        if op == 'S':
            v = int(input('Quantos valores mais? '))
            n = n + v
        elif op != 'S':
            print('Ok! Obrigado por participar!')

    s = s + valor
    i += 1

med = s/n

print('--'*15)
print('A soma é: {} '.format(s))
print('A média é: {}'.format(med))
print('O maior valor é: {}'.format(MAIvalor))
print('O menor valor é: {}'.format(menvalor))

