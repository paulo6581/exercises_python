"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
while True:
    sex = input("Digit your sex: ")
    if sex == 'F':
        print("Feminine")
        break
    elif sex == 'M':
        print("Masculine")
        break
    else: 
        print("Sex INVALID, try again")
print("Hasta la Vista baby, the end programming!")