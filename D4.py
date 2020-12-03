Nome = input('Olá! Digite seu nome para começar: ')
conv = float(input('Boas-vindas {}! Qual a medida que desejas converter? '.format(Nome)))

cm = conv*100
mm = conv*1000

print('Ok! A medida enviada é: {} m'.format(conv))
print('A medida em centímetros: {} cm'.format(cm))
print('A medida em milímetros: {} mm'.format(mm))