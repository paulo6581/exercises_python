"""
2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
print("Cadastro\n")
while True:
    user = input("Digite seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if user.isalnum() and senha.isalnum():
        if user == senha:
            print("ERROR, Digite Novamente!")
            continue 
        elif not user == senha:
            print(f"Conta Criada com sucesso\nusuário: {user}\nsenha: {senha}")
            break
    else:
        print("VOCÊ NÃO DIGITOU NADA!")
