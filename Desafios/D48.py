from datetime import date
maior = 0
menor = 0

for i in range(1, 8):
    p = int(input('Qual o ano de nascimento {}° da pessoa? '.format(i)))
    data = date.today()
    t = (data.year - p)

    if t < 21:
        menor = menor + 1
    elif t >= 21:
        maior = maior + 1

print('--'*10)
print(maior, ' pessoa(s) já atingiu(ram) a maioridade!')
print(menor, ' pessoa(s) ainda não atingiu(ram) a maioridade!')