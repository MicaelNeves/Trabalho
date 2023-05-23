import psycopg2
from Controle.classControle import Conexao
from Modelo.classAluguel import Aluguel
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro


conexaoLivraria = Conexao("ABC Livraria", "localhost", "5432", "postgres", "postgres")


# Menu e funções do cliente


def menuCliente():
    while True:
        print(
            """
        =============OPÇÔES=======================
        1. Ver lista de Aluguéis
        2. Cadastar um cliente de Livro
        3. Informação de um cliente especifico
        4. Atualizar dados Cadastrais
        5. Remover Cliente
        6.Sair
        """
        )

        op = input("Digite uma opção: ")

        match op:
            case "1":
                verlistaclientes()
            case "2":
                cadastrarCliente()
            case "3":
                verClienteEspecifico(input("Digite o id do cliente: "))
            case "4":
                atualizarCliente()
            case "5":
                removerCliente()
            case "6":
                break
            case _:
                print("Erro na operação")


def verlistaclientes():
    listaclientes = conexaoLivraria.consultarBanco(
        """
        SELECT*FROM "Cliente"
        ORDER BY "Id_Livro" ASC
        """
    )

    print("id_Cliente |  Nome do Cliente       |   CPF     ")
    for cliente in listaclientes:
        print(f"   {cliente[0]} |         {cliente[1]}         |   {cliente[2]}       ")


def cadastrarCliente():
    print("=====INICIALIZANDO CADASTRO=======")

    cliente = Cliente(
        None, input("Digite o nome do cliente: "), input("Digite o CPF do cliente: ")
    )
    conexaoLivraria.manipularBanco(cliente.inserirCliente())

    print("=======CADASTRO REALIZADO=========")


def atualizarCliente():
    print("Tela de atualização de cliente:")

    print("Lista de Clientes")

    verlistaClientes()

    clienteEscolhido = input("Digite o id do cliente escolhido:")

    verClienteEspecifico(clienteEscolhido)

    novoNome = input("Digite o novo nome (vazio para não alterar):")
    novoCPF = input("Digite o novo cpf (vazio para não alterar):")

    if novoNome:
        conexaoLivraria.manipularBanco(
            f"""
        UPDATE "Cliente"
        SET "Nome" = '{novoNome}'
        WHERE "Id" = {clienteEscolhido}
        """
        )
    if novoCPF:
        conexaoLivraria.manipularBanco(
            f"""
        UPDATE "Cliente"
        SET "CPF" = '{novoCPF}'
        WHERE "Id" = {clienteEscolhido}
        """
        )

    print("Tentativa de alteração executada.")


def removerCliente():
    print("Tela de remoção de cliente:")

    print("Lista de Clientes")

    verlistaClientes()

    clienteEscolhido = input("Digite o id do cliente escolhido:")

    verClienteEspecifico(clienteEscolhido)

    confirmar = input("Deseja remover este cliente? (S/N)").upper()

    match confirmar:
        case "S":
            resultadoRemocao = conexaoBanco.manipularBanco(
                f"""
           DELETE FROM "Cliente"
           WHERE "Id" = '{clienteEscolhido}'
           """
            )

            if resultadoRemocao:
                print("Cliente removido com sucesso.")
            else:
                print("Cliente não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")


def verClienteEspecifico(idCliente):
    cliente = conexaoLivraria.consultarBanco(
        f"""SELECT * FROM "Cliente"
    WHERE "Id" = {idCliente}
    """
    )

    if cliente:
        cliente = cliente[0]

        print("Cliente Escolhido: ")

        print(
            f"""
        Id - {cliente[0]}
        Nome - {cliente[1]}
        CPF - {cliente[2]}
        """
        )

        listaAlugueis = conexaoLivraria.consultarBanco(
            f"""
        SELECT * FROM "Aluguel"
        WHERE "Id_Cliente" = '{cliente[0]}'
        """
        )
        if listaAlugueis:
            print("Lista de alugueis: ")

            print("ID | Cliente | Livro | Data de Aluguel")
            for aluguel in listaAlugueis:
                # Você já tem o id do Cliente e id do Livro, busque nas tabelas e pegue as informações

                clienteDoAluguel = conexaoLivraria.consultarBanco(
                    f"""
                SELECT * FROM "Cliente"
                WHERE "Id" = {aluguel[1]}
                """
                )[0]

                livroDoAluguel = conexaoLivraria.consultarBanco(
                    f"""
                SELECT * FROM "Catalogo"
                WHERE "Id_Livro" = {aluguel[2]}
                """
                )[0]

                print(
                    f"{aluguel[0]} | {clienteDoAluguel[1]} | {livroDoAluguel[1]} | {aluguel[3]}"
                )
        else:
            print("O cliente não possui aluguéis cadastrados")

    else:
        print("O cliente não foi encontrado!")


# Menu e funções de Aluguel


def menuAluguel():
    while True:
        print(
            """
        =============OPÇÔES=======================
        1. Ver lista de Aluguéis
        2. Cadastar um Aluguel de Livro
       
        3.Sair
        """
        )

        op = input("Digite uma opção: ")

        match op:
            case "1":
                verlistaAluguel()
            case "2":
                cadastrarAluguel()

            case _:
                print("Erro na operação")


def verlistaAluguel():
    listaAluguel = conexaoLivraria.consultarBanco(
        """
        SELECT*FROM "Aluguel"
        ORDER BY "Id_Aluguel" ASC
        """
    )

    print("Nome do Cliente       |   Nome do Livro   |   Data da Entrega")
    for aluguel in listaAluguel:
        nome = conexaoLivraria.consultarBanco(
            f"""
        SELECT*FROM "Cliente"
        WHERE "Id" = {aluguel[1]}
        """
        )[0]
        livro = conexaoLivraria.consultarBanco(
            f"""
        SELECT*FROM "Catalogo"
        WHERE "Id_Livro" = {aluguel[2]}
        """
        )[0]

        print(f"   {nome[1]}    |           {livro[1]}         |   {aluguel[3]}  ")


def cadastrarAluguel():
    while True:
        print("=====INICIALIZANDO CADASTRO DE ALUGUEL=======")

        listaclientes = conexaoLivraria.consultarBanco(
            """
        SELECT*FROM "Cliente"
        ORDER BY "Id" ASC
        """
        )

        print("Id_Cliente  | Nome do Cliente  ")
        for cliente in listaclientes:
            print(f"'{cliente[0]}','{cliente[1]}'")

        listalivros = conexaoLivraria.consultarBanco(
            """
        SELECT*FROM "Catalogo"
        ORDER BY "Id_Livro" ASC
        """
        )

        print("Id_livro | Nome do livro ")
        for livro in listalivros:
            print(f"'{livro[0]}','{livro[1]}'")

        aluguel = Aluguel(
            None,
            input("Digite o id do cliente: "),
            input("Digite o id do livro: "),
            None,
        )
        conexaoLivraria.manipularBanco(aluguel.inserirAluguel())
        print("=======CADASTRO REALIZADO=========")

        op = input("Você desejar continuar a operacão de outro aluguel? [S] [N]")

        if op.upper() == "S":
            pass
        elif op.upper() == "N":
            print("Voltando ao menu principal...")
            break
        else:
            print("Falha na operação")


# Menu e funções de Livros


def menuLivro():
    while True:
        print(
            """
        =============OPÇÔES=======================
        1. Ver lista de livros do Acervo
        2. Cadastar um novo Livro
        
        3.Sair
        """
        )

        op = input("Digite uma opção: ")

        match op:
            case "1":
                verlistaLivros()
            case "2":
                cadastroLivro()
            case _:
                print("Erro na operação")


def cadastroLivro():
    print("=====INICIALIZANDO CADASTRO=======")

    livro = Livro(
        None,
        input("Digite o título do livro: "),
        input("Digite o autor do livro: "),
        input("Digite o preco do livro: "),
        input("Digite a quantidade no estoque livro: "),
    )
    conexaoLivraria.manipularBanco(livro.inserirLivro())

    print("=======CADASTRO REALIZADO=========")


def verlistaLivros():
    listaLivros = conexaoLivraria.consultarBanco(
        """
        SELECT*FROM "Catalogo"
        ORDER BY "Id_Livro" ASC
        """
    )

    print(
        "id_Livro |  Nome do Livro       |   Nome do autor   |   Preco  |   Estoque   "
    )
    for livro in listaLivros:
        print(
            f"   {livro[0]} |         {livro[1]}         |   {livro[2]}       |  {livro[3]}    |   {livro[4]}  "
        )


# Criação  de Tabelas


def CriarTabelas(aux):
    while aux < 2:
        try:
            conexaoLivraria.manipularBanco(Cliente.criarTabelaCliente())
            conexaoLivraria.manipularBanco(Livro.criarTabelaLivro())
            conexaoLivraria.manipularBanco(Aluguel.criarTabelaAluguel())
            print("Tabelas Criadas com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Algo deu Errado! ", error)

        aux += 1


# CriarTabelas(1)


# Menu Principal do programa


def TelaPrincipal():
    while True:
        print(
            """
            
            BEM-VINDO A ABC LIVRARIA
            -----======================----

            Qual Menu você desejar visualizar?

            1. Menu de Clientes
            2. Menu de Livros
            3. Menu Aluguel
            0. Sair

            """
        )

        op = input("Digite a ação que deseja realizar? ")

        match op:
            case "1":
                menuLivro()
            case "2":
                menuCliente()
            case "3":
                menuAluguel()
            case "0":
                print("Voce Finalizou a consulta!")
                break


TelaPrincipal()
