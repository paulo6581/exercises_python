"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
num1 = input("Digit a number one: ")
num2 = input("Digit a number two: ")
num3 = input("Digit a number three: ")
if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    if num1 > num2 and num1 > num3 or not(num1 > num2 and num1 > num3):
        if num1 > num2 and num1 > num3:
            print(f"{num1} maior")
        elif not(num1 > num2 and num1 > num3):
            print(f"{num1} menor")
    elif num2 > num1 and num2 > num3 or not(num2 > num1 and num2 > num3):
        if num2 > num1 and num2 > num3:
            print(f"{num2} maior")
        elif not(num2 > num1 and num2 > num3):
            print(f"{num2} menor")
    elif num3 > num1 and num3 > num2 or not(num3 > num1 and num3 > num2):
        if num3 > num1 and num3 > num2:
            print(f"{num3} maior")
        elif not(num3 > num1 and num3 > num2):
            print(f"{num3} menor")
    
else:
    print("INVALID")

# não finalizado