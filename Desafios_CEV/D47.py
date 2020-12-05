f = str(input('Digite a frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inv = ''

for i in range(len(j) -1, -1, -1):
    inv = inv + j[i]

if j == inv:
    print('É UM PALÍNDROMO!')
else:
    print('NÃO É UM PALÍNDROMO')