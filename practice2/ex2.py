"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
while True:
    value = input("Digit a number: ")
    if value.isdigit():
        value = int(value)
        if value >= 0:
            print(f"{value} is positive!")
            break
        elif value <0:
            print(f"{value} is negative!")
            break
    else:
        print("Invalid, try again")
        continue
print("The End Programming!")