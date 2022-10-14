"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    name = input("Digite seu nome: ")
    idade = input("Digite a sua idade: ")
    salary = input("Digite seu salário: ")
    sexo = input("Digite seu sexo:\nmasculino = {m}\nfeminino = {f}\nDigite: ")
    civil = input("Digite seu estado civil:\nsolteiro = {s}\ncasado = {c}\nviúvo = {v}\ndivorciado = {d}\nDigite: ")
    if idade.isnumeric and salary.isnumeric():
        idade = int(idade)
        salary = int(salary)
        if (len(name) > 3) and (idade > 0 and idade > 0 and idade < 151) and (salary > 0) and (sexo == 'f' or sexo == 'm') and (civil == 's' or civil == 'c' or civil == 'v' or civil == 'd'):
            print(f"\n\nVÁLIDO:\n{name}\n{idade}\n{salary}\n{sexo}\n{civil}")
            break
        else:
            print("ERRO, inválido, digite novamente!")
    else:
        print("ERRO, Número string")