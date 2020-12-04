Nome = input('Boas-vindas viajante! Como se chamas? ')
frase = input('Prazer, {}! Tu queres dizer algo?? '.format(Nome))

f = frase.count('a')
f = f + frase.count('A')
F = frase.upper()
FA = F.find('A')
FAR = F.rfind('A')

print('{:=^25}'.format(''))
print("Vamos ver...você falou {} A's!".format(f))
print('A letra A aparece pela 1°vez na  posição [{}]'.format(FA))
print('A letra A aparece pela última vez na posição [{}]'.format(FAR))