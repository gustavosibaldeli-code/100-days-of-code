# Sistema de Cadastro de Aluno

alunos = []

while True:
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastrar aluno
    if opcao == "1":
        print("\n===== CADASTRAR ALUNO =====")

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")

        novo_aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso
        }

        alunos.append(novo_aluno)

        print("\nAluno cadastrado com sucesso!")

    # Listar alunos
    elif opcao == "2":
        print("\n===== LISTA DOS ALUNOS =====")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for numero, aluno in enumerate(alunos, start=1):
                print(f"\nAluno {numero}")
                print(f"Nome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Curso: {aluno['curso']}")

    # Buscar aluno
    elif opcao == "3":
        print("\n===== BUSCAR ALUNO =====")

        nome_busca = input("Digite o nome do aluno: ")

        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == nome_busca.lower():
                print("\nAluno encontrado!")
                print(f"Nome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Curso: {aluno['curso']}")

                encontrado = True
                break

        if not encontrado:
            print("\nAluno não encontrado.")

    # Remover aluno
    elif opcao == "4":
        print("\n===== REMOVER ALUNO =====")

        remover_aluno = input("Digite o nome do aluno que deseja remover: ")

        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == remover_aluno.lower():
                alunos.remove(aluno)

                print("\nAluno removido com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("\nAluno não encontrado.")

    # Sair
    elif opcao == "5":
        print("\nEncerrando sistema...")
        break

    else:
        print("\nOpção inválida. Escolha uma opção de 1 a 5.")  