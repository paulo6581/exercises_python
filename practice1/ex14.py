"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
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

weight_fish = input('Digite o peso dos peixes: ')
if is_number(weight_fish):
    weight_fish = float(weight_fish)
    if weight_fish>50:
        excess = weight_fish - 50
        multa = excess*4.00
        print(f'O valor da multa é R${multa:.2f}')
    else:
        print(f'Não excedeu, o peso do peixe é {weight_fish} Kg')
else:
    print('Erro, inválido, digite novamente')