print('FIBONACCI')
print('--'*15)
print('Bem-vindo(a)!')
t = int(input('Quantos termos do FIBONACCI você deseja? '))

i = 0
a = 0
b = 1

while i < t:
    i = i +1

    c = b + a
    a = b
    b = c
    print(a)