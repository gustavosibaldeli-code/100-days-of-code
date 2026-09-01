# Sistema de Login — Dia 5

import bcrypt
import os

usuarios = []

# Carregar usuários do arquivo
if os.path.exists("usuarios.txt"):
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha:
                usuario, senha_hash = linha.split(":", 1)

                usuarios.append({
                    "usuario": usuario,
                    "senha": senha_hash.encode("utf-8")
                })


while True:
    print("\n===== SISTEMA DE LOGIN =====")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastro de usuário
    if opcao == "1":
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")

        # Verificar se o usuário já existe
        usuario_existe = False

        for usuario_cadastrado in usuarios:
            if usuario_cadastrado["usuario"] == usuario:
                usuario_existe = True
                break

        if usuario_existe:
            print("Esse usuário já está cadastrado!")

        else:
            senha_hash = bcrypt.hashpw(
                senha.encode("utf-8"),
                bcrypt.gensalt()
            )

            usuarios.append({
                "usuario": usuario,
                "senha": senha_hash
            })

            # Salvar usuário no arquivo
            with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(
                    f"{usuario}:{senha_hash.decode('utf-8')}\n"
                )

            print("Usuário cadastrado com sucesso!")

    # Login de usuário
    elif opcao == "2":
        usuario_login = input("Digite o usuário: ")
        senha_login = input("Digite a senha: ")

        encontrado = False

        for usuario in usuarios:
            if usuario["usuario"] == usuario_login:

                if bcrypt.checkpw(
                    senha_login.encode("utf-8"),
                    usuario["senha"]
                ):
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
