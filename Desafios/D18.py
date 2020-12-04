Nome = input('Boas-vindas viajante! Como se chamas? ')
Reino = input('Prazer, {}! De que reino vens? '.format(Nome))

l = 'Santo' in Reino
print('Vamos ver...há Santo no nome de seu reino? {}'.format(l))