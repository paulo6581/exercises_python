"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
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

num = input('Digite um valor: ')

if is_number(num):
    num = float(num)

