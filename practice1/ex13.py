"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
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

height = input('Digite a sua altura: ')

if is_number(height):
    height = float(height)
    man =  (72.7*height)-58
    women = (62.1*height)-44.7
    print(f'Homem: {man:.2f}')
    print(f'Mulher: {women:.2f}')
else:
    print('Erro, inválido')