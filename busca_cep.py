import requests

def buscar_cep():
    print("=== BUSCADOR DE ENDEREÇO (VIA CEP) ===")

    while True:
        cep_usuario = input("\nDigite o CEP para busca (apenas números): ").strip()

        cep_limpo = cep_usuario.replace("-", "").replace(".", "")

        if len(cep_limpo) != 8 or not cep_limpo.isdigit():
            print("Erro: Digite um CEP válido com exatamente 8 números!")
            continue

        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

        try:
            repostas = requests.get(url, timeout=5)
            dados = repostas.json()

            if "erro" in dados:
                print("CEP não encontrado na base de dados!")
                continue

            print("\n Endereço Encontrado:")
            print(f" • Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f" • Bairro:     {dados.get('bairro', 'N/A')}")
            print(f" • Cidade:     {dados.get('localidade', 'N/A')}")
            print(f" • Estado:     {dados.get('uf', 'N/A')}")
            print(f" • DDD:        {dados.get('ddd', 'N/A')}")

        except requests.exceptions.RequestException as e:
            print(f" Erro de conexão com a API: {e}")

        opcao = input("\nDeseja buscar outro CEP? (s/n): ").strip().lower()

        if opcao != 's':
            print("\nObrigado por usar o Buscador de CEP! Programa encerrado.")
            break

if __name__ == "__main__":
    buscar_cep()