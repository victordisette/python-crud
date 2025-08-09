print("--- TELA DE CADASTRO ---")

cadastro = []

while True:
    print("=== Gerenciador de Contatos ===")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Atualizar contato")
    print("4 - Excluir contato")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1": 
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu Email: ")
        cadastro.append([nome, telefone, email])
        print("Contato cadastrado com sucesso!\n")

    elif escolha == "2":
        if not cadastro:
            print("\nNENHUM DADO CADASTRADO!!!")
        else:
            print("Lista de contatos:")
            for i, cadastros in enumerate(cadastro):
                print(f"{i} - Nome: {cadastros[0]}, Telefone: {cadastros[1]}, E-mail: {cadastros[2]}")
            print()

    elif escolha == "3":
        if not cadastro:
            print("Nenhum contato para ser atualizado!!\n")
            continue
        else:
            print("Contatos a serem atualizados:")
            for i, cadastros in enumerate(cadastro):
                print(f"{i} - Nome: {cadastros[0]}, Telefone: {cadastros[1]}, E-mail: {cadastros[2]}")
            indice = input("Digite o número do contato que deseja atualizar: (obs: digite apenas número) ")
            if not indice.isdigit():
                print("Entrada inválida!!\n")
                continue
            indice = int(indice)

            if 0 <= indice < len(cadastro):
                print("Qual campo deseja atualizar?")
                print("0 - [  Nome ]")
                print("1 - [ Telefone ]")
                print("2 - [ E-mail ]")

                campo = input("Digite o Número a ser atualizado: ")
                if not campo.isdigit():
                    print("VALOR INVÁLIDO\n")
                    continue
                campo = int(campo)

                if campo in (0, 1, 2):
                    novo_valor = input("Digite o novo valor: ")
                    cadastro[indice][campo] = novo_valor
                    print("Contato atualizado com sucesso!\n")
                else:
                    print("Campo inválido.\n")
            else:
                print("Índice inválido.\n")

    elif escolha == "4":
        if not cadastro:
            print("Nenhum contato para excluir.\n")
            continue
        print("Contatos disponíveis:")
        for i, contato in enumerate(cadastro):
            print(f"{i} - Nome: {contato[0]}, Telefone: {contato[1]}, E-mail: {contato[2]}")

        indice = input("Digite o índice do contato que deseja excluir: ")
        if not indice.isdigit():
            print("Entrada inválida! Digite um número.\n")
            continue
        indice = int(indice)

        if 0 <= indice < len(cadastro):
            cadastro.pop(indice)
            print("Contato excluído com sucesso!\n")
        else:
            print("Índice inválido.\n")

    elif escolha == "5":
        print("Saindo do programa...")
        break # sinal de pare 

    else:
        print("Opção inválida, tente novamente.\n")
