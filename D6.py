Nome = input('Olá! Como você se chama, caro amigo? ')
valor = float(input('Ok! Boas-vindas {}! Que valor tu desejas ter em dólares: '.format(Nome)))

dol = valor/3.27

print('Você tem: R$ {}'.format(valor))
print('Equivalentes a: U$ {:.2f}'.format(dol))