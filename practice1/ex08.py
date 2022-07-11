"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
gain_hour = float(input('Digite o quando você ganha por hora: '))
work_hours = int(input('Digite o número de horas trabalhadas no mês: '))
gain_month = work_hours*gain_hour
"""
1h ---- gain_hour
work_hours -- gain_month

gain_month = work_hours * gain_hour
"""
print(f'Salário: R${gain_month}')