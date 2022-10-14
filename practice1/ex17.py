"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

- Resolução
    .rende a tinta: 
        1l de tinta - 6m² (unitário)
        1 lata rende: 18l - 108m²
        1 galão rende: 3,6l - 21m²

    .Preços:
        1 lata 18l = R$80,00
        1 galão 3,6l = R$25,00 
- Equation: 
    x = area/6 => x_litros

1 lata ------ 18 l
 nº latas ----- x_litros
 nº latas = x_litros/18 

price_latas = nª latas * 80
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

area = input('Informe a área a ser pintada: ')
if is_number(area):
    area = float(area)
    x_litros = area/6   
    arrendonda_10 = (x_litros*10)/100
    # Apenas latas                                       
    if x_litros >= 18: 
        n_latas = round(x_litros/18)
        print(f'Compre {n_latas} latas de 18 litros.')
        if x_litros+arrendonda_10 >= 21.6:
            mistura = round(x_litros/21.6)
            print(f'Compre {mistura} de latas e galões.')
    # Apenas galões
    elif x_litros < 18 and x_litros >= 3.6:
        n_galoes = round(x_litros/3.6)
        print(f'Compre {n_galoes} galões de 3,6 litros.')
    # mistura - latas e galões
else:
    print('ERRO, inválido, digite novamente')