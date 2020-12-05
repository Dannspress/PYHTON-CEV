from math import sqrt
n = int(input('Digite um número: '))
raiz = sqrt(n)
print("A raiz de {} é: {:.3f}".format(n, raiz))

import random
m = random.random()
print(m)

v = random.randint(1, 10)
print(v)

import emoji
print(emoji.emojize("Olá! Você aceita um café? :coffee:", use_aliases=True))