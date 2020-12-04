Nome = str(input('Como você se chama? '))
Nome = Nome.capitalize()
if Nome == 'Dan':
    print('Uau! Você é o namorado da Andressa? ')
else:
    print('Ah sim....')

N1 = float(input('Como você foi no semestre? Qual foi a primeira nota? '))
N2 = float(input('Hm.. interessante. E a segunda nota, quanto? '))
M = (N1+N2) / 2

print("{:=^20}".format(''))
print('Então sua média foi {}?'.format(M))
if M >= 7.0:
    print('Você passou! Parabéns!!')
else:
    print('Bah, você reprovou..')
print("{:=^20}".format(''))
