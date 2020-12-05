soma = 0
for i in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n %2 == 0:
        soma = soma + n

print('A soma dos pares é: {}'.format(soma))