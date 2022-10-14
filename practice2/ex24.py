"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
print('Digite SIM = [1] e Não = [0]:\n')
tel = int(input('Telefonou para a vítima?\n'))
local = int(input('Esteve no local do crime?\n'))
mora = int(input('Mora perto da vítima?\n'))
dev = int(input('Devia para a vítima?\n'))
trab = int(input('Já trabalhou com a vítima?\n'))

soma = tel + local + mora + dev + trab 

if soma == 2:
    print('Suspeito')
if soma == 3 or soma == 4:
    print('Cúmplice')
if soma == 5:
    print('Assassino')
if soma == 1  or soma == 0:
    print('Inocente')

