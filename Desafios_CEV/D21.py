Nome = input('Boas-vindas viajante! Como se chamas? ')
print('Prazer, {}!'.format(Nome))

DNome = Nome.split()
PNome = DNome[0]
u = len(DNome)
# UNome = DNome[u]

print('{:=^25}'.format(''))
print('Seu primeiro nome é: {}'.format(PNome))
print('Seu último nome é: {}'.format(DNome[u-1]))