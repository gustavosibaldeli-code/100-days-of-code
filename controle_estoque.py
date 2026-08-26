# Sistema de Cadastro de Produtos com Arquivo TXT

import os

produtos = []

ARQUIVO = "produtos.txt"


# Carregar produtos do arquivo

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha:
                nome, preco, quantidade = linha.split("|")

                produto = {
                    "produto": nome,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                }

                produtos.append(produto)


while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Excluir produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastrar Produto
    if opcao == "1":

        print("\n===== CADASTRAR PRODUTO =====")

        produto = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        novo_produto = {
            "produto": produto,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(novo_produto)

        # Salvar no arquivo
        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"{produto}|{preco}|{quantidade}\n"
            )

        print("Produto cadastrado com sucesso!")


    # Listar Produtos
    elif opcao == "2":

        print("\n===== LISTAR ESTOQUE =====")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")

        else:
            for numero, produto in enumerate(produtos, start=1):

                print(f"\nProduto {numero}")
                print(f"Nome: {produto['produto']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")


    # Buscar Produto
    elif opcao == "3":

        print("\n===== BUSCAR PRODUTO =====")

        busca_produto = input("Digite o nome do produto: ")

        encontrado = False

        for produto in produtos:

            if produto["produto"].lower() == busca_produto.lower():

                print("\nProduto encontrado!")
                print(f"Nome: {produto['produto']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")

                encontrado = True
                break

        if not encontrado:
            print("\nProduto não encontrado.")


    # Excluir Produto
    elif opcao == "4":

        print("\n===== EXCLUIR PRODUTO =====")

        remover_produto = input(
            "Digite o nome do produto que deseja excluir: "
        )

        encontrado = False

        for produto in produtos:

            if produto["produto"].lower() == remover_produto.lower():

                produtos.remove(produto)

                # Atualizar o arquivo
                with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

                    for item in produtos:
                        arquivo.write(
                            f"{item['produto']}|"
                            f"{item['preco']}|"
                            f"{item['quantidade']}\n"
                        )

                print("\nProduto removido com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("\nProduto não encontrado.")


    # Sair
    elif opcao == "5":

        print("\nEncerrando sistema...")
        break


    else:

        print("\nOpção inválida. Escolha uma opção de 1 a 5.")