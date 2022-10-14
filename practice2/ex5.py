"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
while True:
    note1 = input("Digit yours note one: ")
    note2 = input("Digit yours note two: ")
    if note1.isdigit() and note2.isdigit():
        note1 = float(note1)
        note2 = float(note2)
        media = (note1 + note2)/2
        if media >= 7 and media <10:
            print("Approved")
            break
        elif media == 10:
            print("Approved with distinction")
            break
        elif media < 7:
            print("Reproved")
            break
    else: 
        print("INVALID")
        continue
