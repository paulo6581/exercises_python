"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
import re
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)

num1 = input('Digite um número inteiro: ')
num2 = input('Digite o segundo número inteiro: ')
num3 = input('Digite um número real: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    res1 = 2*num1*num2/2
    print(f'Result do Cálculo 1: {res1}')
    if is_number(num3):
        num3 = float(num3)
        res2 = (3*num1)+num3
        print(f'Resultado do Cálculo 2: {res2:.3f}')
    else:
        print('ERRO, digite apenas valores reais.')
else: 
    print('ERRO, INVÁLIDO O VALOR, valores apenas inteiros.')
