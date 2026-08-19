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


        # Listar Aluno 
    elif opcao == "2":
        print("\n===== LISTA DOS ALUNOS =====")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for novo_aluno, aluno in enumerate(alunos, start=1):
                print(f"{novo_aluno}. {aluno}")


       # Buscar Aluno

    elif opcao == "3":
        print("\n===== SEU ALUNO =====")

        if len(alunos) == 0:
            print("Nenhum aluno encontrado com esse nome.")
        else:
            for nome, aluno in enumerate(alunos, start=1):
                print(f"{nome}. {aluno}")


      # Remover Aluno
    elif opcao == "4":
        print("\n===== REMOVA O ALUNO  =====")

        remover_aluno = input("Remova o aluno desejado:")

        if remover_aluno in alunos:
            alunos.remove(remover_aluno)
            print("Aluno removido com sucesso!")

        else:
            print("Aluno não encontrado.")

      # Sair

    elif opcao =="5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 5.")

