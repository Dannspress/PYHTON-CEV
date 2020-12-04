t = 0
n = int(input('Digite um número: '))
print('--'*12)

for i in range(1, n+1):
    if 0 == (n%i):
        t = t + 1

if t == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')