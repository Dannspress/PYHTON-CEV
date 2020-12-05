frase = 'Curso em Vídeo Python'
# print(frase[3])
# print(frase[3:13])
# print(frase[:13])
# print(frase[13:])
# print(frase[1:15:2])
# print(frase[3::2])
# print(frase[::3])

print(frase.count('o'))
print(len(frase))
print(frase.replace('Curso', 'Café'))

dividido = frase.split()
print(dividido[2][3])
# [2] = Palavra separada 'Vídeo'
# [3] = Posição da palavra [2]