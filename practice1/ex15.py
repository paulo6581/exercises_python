"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
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

hour_salary = input('Quanta você ganha por hora?\n')
hours_month = input('Quantas horas trabalhadas no mês?\n')

if is_number(hour_salary) and is_number(hours_month):
    hour_salary = float(hour_salary)
    hours_month = int(hours_month)
    total_salary = hour_salary*hours_month
    
    ir = (total_salary*11/100)
    inss = (total_salary*8/100)
    sin = (total_salary*5/100)
    sal_liq = total_salary-ir-inss-sin
    text = '= Resultado ='
    print(f'{text:_^70}') # output - message of the text: result
    print(f'\n+ Salário bruto: R${total_salary:.2f}\nIMPOSTO É ROUBO\n- IR (11%): R${ir:.2f}\n- INSS (8%): R${inss:.2f}\n- Sindicato (5%): R${sin:.2f}\n= Salário líquido: R${sal_liq:.2f}')