Nome = input('Olá! Como você se chama? ')
D = int(input('{}, sua viagem tem quantos quilômetros? '.format(Nome)))

print("{:=^20}".format(''))
if D >= 200:
    precA = D * 0.45
    print('Uau! Viagem longa em? A passagem custa: R$ {:.2f}'.format(precA))
else:
    precB = D * 0.50
    print('Ok! Aqui está o valor da passagem: R$ {:.2f}'.format(precB))