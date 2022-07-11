"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

v = space/time  =>  vel_link = tam_mb/tim_aprox  =>  time_aprox = tam_mb/vel_link
1 byte = 8 bits
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

tam_mb = input('Digite o tamanho do arquivo em MB: ')  # MB = Megabyte = 1x10
vel_link = input('Digite a velocidade do link em Mbps: ')  # Mbps = megabit por segundo

if is_number(tam_mb) and is_number(vel_link):
    tam_mb = float(tam_mb)
    vel_link = float(vel_link)
    vel_link = vel_link/8
    time_aprox = (tam_mb/vel_link)/60
    print(f'O Tempo aproximado do download: {time_aprox:.0f} minutos.')