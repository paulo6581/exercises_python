"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
c = input('Digite a temperatura em Celsius: ')
if c.isdigit():
    c = float(c)
    f = (9*c+160)/5
    print(f'Fahrenheit: {f:.1f} °F')
else:
    print('Erro, digite números!')