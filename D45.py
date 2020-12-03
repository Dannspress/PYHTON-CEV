n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
print('--'*15)
print('Subtrair ou Somar? ')
print('--'*15)
print('1 - Somar:')
print('2 - Subtrair:')
sinal = int(input('Opção: '))
print('--'*15)
print('PA:')
print('--'*15)
print(n)
if sinal == 1:
    for i in range(1, 10):
        n = n + r
        print(n)
elif sinal == 2:
    for i in range(1, 10):
        n = n - r
        print(n)
else:
    print('OPÇÃO INVÁLIDA')