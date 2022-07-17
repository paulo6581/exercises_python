"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        print(f'O número {num1} é maior.')
    elif num1 < num2:
        print(f'O número {num2} é maior.')
else:
    print('ERRO, inválido, digite novamente')