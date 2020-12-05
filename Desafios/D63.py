dezoi = hom = f20 = 0

while True:
    print('--'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())
    op = str(input('Quer continuar [S/N]? ').upper())

    if idade > 18:
        dezoi += 1

    if sexo == 'M':
        hom += 1

    if idade <= 20 and sexo == 'F':
        f20 += 1

    if op == 'N':
        print(f'O número de pessoas maiores de 18 é: {dezoi}')
        print(f'O número de homens é: {hom}')
        print(f'O número de mulheres de até 20 anos é: {f20}')
        break
