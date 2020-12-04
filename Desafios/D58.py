print('Bem-vindo(a)!')
n = int(input('Quantos números você deseja somar? '))
s = 0
i = 1
sn = 0
valor = 0

while i <= n and valor < 999 and s <= 999:
    valor = int(input('Qual o {}° valor? '.format(i)))
    s = s + valor
    i += 1
    sn = sn + 1
if valor == 999:
    print('Você interrompeu o processo!')
    print('--'*15)

if s >= 999:
    print('Você alcançou/ultrapassou a soma de 999!')

print('Você escreveu {} números, os quais somando é: {} '.format(sn, s))

