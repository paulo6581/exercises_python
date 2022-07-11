"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
1 l ------- 3m² 
18 l ------ x 
x = 18 * 3
x = 54 m²

A lata de tina: 
18 litros
área = 54 m²
custa = R$80,00
----------------
num_latas = area/54 
"""
area = float(input('Digite a área da sua casa: '))
lata_1 = 18 
num_latas = round(area/54)
preco_total = num_latas*80

print(f'Número de latas: {num_latas}\npreço total: R${preco_total}')