"""
Faça um Programa que leia três números e mostre o maior deles.
"""
while True:
    num1 = input("Digit a number one: ")
    num2 = input("Digit a number two: ")
    num3 = input("Digit a number three: ")
    if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        if num1 > num2 and num1> num3:
           print(num1)
           break
        elif num2 > num1 and num2 > num3:
            print(num2)
            break
        elif num3 > num1 and num3 >num2:
            print(num3)
            break
    else:
        print("INVALID")
        continue