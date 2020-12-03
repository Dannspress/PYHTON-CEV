from datetime import date
id = 0
inv = 0
tid = 0
m20 = 0
maior = ''

for i in range(1, 5):
    nome = str(input('{}° PESSOA: Qual é o seu nome? '.format(i)))
    idade = int(input('{}° PESSOA: Qual é a sua idade? '.format(i)))
    sexo = str(input('{}° PESSOA: Qual é o seu sexo (M/F))? '.format(i))).upper()
    print('--'*15)

    # Errar sexo
    if sexo != 'M' and sexo != 'F':
        inv = inv + 1

    # Total das Idades
    tid = tid + idade

    # Mulheres com menos de 20 anos
    if sexo == 'M' and idade < 20:
        m20 = m20 + 1

    # Nome do mais velho sendo o primeiro dado
    if i == 1:
        maior = nome

    # Nome do mais velho
    if idade > id:
        maior = nome

#Média das idades
md = (tid/4)

print('A média da idade do grupo é: ', md)
print('O nome do mais velho é: ', maior)
print('O número de mulheres com menos de 20 anos é: ', m20)