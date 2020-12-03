n = int(input("Digite um número: "))
i = n + 1
total = 1
while i > 1:
    i = i - 1
    total = total*i

print('O fatorial de {} é: {}'.format(n, total))