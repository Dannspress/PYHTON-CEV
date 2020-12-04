Nome = str(input('Olá! Como você se chama? '))
h = float(input('Prazer, {}! Qual é a sua altura? '.format(Nome)))
p = float(input('E seu peso? '))

IMC = p / h**2
print('--' * 20)
print('Seu peso: {} Kg'.format(p))
print('Sua altura: {}'.format(h))
print('Seu IMC: {:.2f}'.format(IMC))
print('--' * 20)

if IMC < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= IMC < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= IMC < 30:
    print('Você está em SOBREPESO!')
elif 30 <= IMC < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')