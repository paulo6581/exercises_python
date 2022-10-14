"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
"""
while True:
    nota = input("Digit a nota: ")
    if nota.isnumeric(): 
        nota = int(nota)
        if nota>=0 and nota<=10:
            print(f"The numeric {nota}")
            break
        else:   
            print("INVALID, digit try again")
            continue
    else: 
        print("ERROR, not is numeric")
print("The End Programming")