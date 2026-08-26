# Sistema de Login
import bcrypt

usuarios = []

while True:
    print("\n===== SISTEMA DE LOGIN =====")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastro Usuario

    if opcao == "1":
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")

        usuarios.append({
            "usuario": usuario,
            "senha": senha
        })

        print("Usuário cadastrado com sucesso!")

    # Login usuario

    elif opcao == "2":
        usuario_login = input("Digite o usuário: ")
        senha_login = input("Digite a senha: ")

        encontrado = False

        for usuario in usuarios:
            if usuario["usuario"] == usuario_login and usuario["senha"] == senha_login:
                encontrado = True
                break

        if encontrado:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos!")

    # Listar usuários

    elif opcao == "3":
        print("\n===== LISTAR USUÁRIOS =====")

        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")

        else:
            for numero, usuario in enumerate(usuarios, start=1):
                print(f"\nUsuário {numero}")
                print(f"Nome: {usuario['usuario']}")

    # Sair

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("\nOpção inválida. Escolha uma opção de 1 a 4.")