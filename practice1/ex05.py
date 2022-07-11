"""
Faça um Programa que converta metros para centímetros.
"""
metros = float(input('Digite um número: '))
centi = metros*100
"""
-> Exemplo: 
1 m = 100 cm
metros = ?

1 m ------- 100 cm
metros ------  x centi
x centi = centi * 100
x centi = 100 * centi
"""
print(f'{centi:.2f} cm')