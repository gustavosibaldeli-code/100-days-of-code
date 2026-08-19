# GERENCIADOR DE TAREFAS

tarefas = []

while True:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # ADICIONAR TAREFA
    if opcao == "1":
        nova_tarefa = input("Digite a tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    # LISTAR TAREFAS
    elif opcao == "2":
        print("\n===== SUAS TAREFAS =====")

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                print(f"{numero}. {tarefa}")

    # REMOVER TAREFA
    elif opcao == "3":
        remover_tarefa = input("Digite a tarefa que deseja remover: ")

        if remover_tarefa in tarefas:
            tarefas.remove(remover_tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Essa tarefa não existe.")

    # SAIR
    elif opcao == "4":
        print("Encerrando sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")