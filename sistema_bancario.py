
# Importa o módulo textwrap para manipulação de strings de menu
import textwrap



# Exibe o menu principal e retorna a opção escolhida pelo usuário

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))



# Realiza um depósito na conta
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor  # Adiciona o valor ao saldo
        extrato += f"Depósito:\tR$ {valor:.2f}\n"  # Registra no extrato
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato  # Retorna saldo e extrato atualizados



# Realiza um saque da conta
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo
    excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite permitido
    excedeu_saques = numero_saques >= limite_saques  # Verifica se já atingiu o limite de saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor  # Subtrai o valor do saldo
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"  # Registra no extrato
        numero_saques += 1  # Incrementa o número de saques
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato  # Retorna saldo e extrato atualizados



# Exibe o extrato da conta
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")



# Cria um novo usuário e adiciona à lista de usuários
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")



# Busca um usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



# Cria uma nova conta para um usuário existente
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")



# Lista todas as contas cadastradas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



# Função principal que executa o sistema bancário
def main():
    LIMITE_SAQUES = 3  # Número máximo de saques diários
    AGENCIA = "0001"  # Código da agência padrão

    saldo = 0  # Saldo inicial
    limite = 500  # Limite máximo por saque
    extrato = ""  # Histórico de operações
    numero_saques = 0  # Contador de saques
    usuarios = []  # Lista de usuários
    contas = []  # Lista de contas

    while True:
        opcao = menu()  # Exibe o menu e lê a opção do usuário


        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break  # Sai do loop e encerra o programa

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Inicia o programa principal
main()
