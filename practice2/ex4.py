"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
while True:
    letter = input("Digit a letter: ")
    if letter.isalpha():
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u') or (letter == 'A' or letter == 'E'or letter == 'I' or letter == 'O' or letter == 'U'):
            print(f"\nThe letter '{letter}' is vowel")
            break
        else: 
            print(f"\nThe letter '{letter}' is consonant")
            break
    else: 
        print("INVALID")
        continue
print("The end programming!")