soma = 0

for i in range(1, 500):
    if i %2 == 1 and i %3 == 0:
        soma = soma + i

print('A soma total é: {}'.format(soma))