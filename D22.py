from random import randint
from time import sleep

Nome = input('Olá! Como você se chama? ').upper()
print('Prazer, {}! Eu irei sortear um número, você consegue adivinhar qual? '.format(Nome))

num = randint(0, 5)
tent = int(input('De 0 a 5, que número foi sorteado? '))
print('LOADING...')
sleep(2)

print('-==-' * 20)
if tent == num:
    print('Você colocou {}? PARABÉNS! Você venceu!'.format(tent))
else:
    print('Você colocou {}? Que pena..era {}! Você perdeu.'.format(tent, num))