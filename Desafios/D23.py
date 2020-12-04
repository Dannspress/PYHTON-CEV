Nome = input('Olá! Como você se chama? ')
V = int(input('Em que velocidade você estava dirigindo, {}? '.format(Nome)))

print("{:=^20}".format(''))
if V > 80:
    acima = V - 80
    multa = acima * 7.00
    print('Dirigindo a {} Km/h ?! Infelizmente aqui está sua multa de: R$ {:.2f}'.format(V, multa))
else:
    print('Dirigindo a {} Km/h ? Tudo bem, siga em frente!'.format(V))