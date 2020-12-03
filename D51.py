Sex = 'X'

while Sex != 'F' and Sex != 'M':
    Sex = input("Qual é o seu sexo [M/F] ? ").upper()

if Sex == 'F':
    print('Bem-vinda!')
elif Sex == 'M':
    print('Bem-vindo!')