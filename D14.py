from random import shuffle
A1 = input('Digite o nome do 1°Aluno: ')
A2 = input('Digite o nome do 2°Aluno: ')
A3 = input('Digite o nome do 3°Aluno: ')
A4 = input('Digite o nome do 4°Aluno: ')

lista = [A1, A2, A3 ,A4]
shuffle(lista)

print('{:=^25}'.format(''))
print('A ordem de apresentação é:')
print('{:=^25}'.format(''))
print(lista)