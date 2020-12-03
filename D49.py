menor = 0
maior = 0

for i in range(1, 6):
    p = float(input('Digite o {}° peso, em Kg: '.format(i)))
    if i == 1:
        menor = p
        
    if p > menor and p > maior:
        maior = p
    elif p < menor and p > 0:
        menor = p

print('--'*10)
print('O menor peso é: ', menor)
print('O maior peso é: ', maior)