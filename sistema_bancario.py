menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0 #Começa com 0 pois o usuário tem que colocar seu primeiro deposito 
limite = 500 #Limite de 500 por saque
extrato = "" #Lista todos os depositos e saques, se o extrato estiver em branco tem que aparecer a mensagem: Não foram realizadas movimentações
numero_saques = 0 #Variavel para armazenar o numero de saques
LIMITE_SAQUES = 3 #Limite de saques diarios

while True:

    opcao = int(input(menu)) #Mostra o menu, e vai receber um numero inteiro

    if opcao == 1: #Deposito    
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: #Se o valor informado for maior que 0, então esse valor é adicionado na variavel saldo
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" #Guarda a movimentação no extrato

        else:
            print("Operação falhou! O valor informado é inválido.") #Caso insira um valor menor que 0, a operação falha 

    elif opcao == 2: #Saque
        valor = float(input("Informe o valor do saque: ")) 

        if valor > saldo: #Verifica se o valor informado foi maior que o saldo existente na conta, se for a operação falha
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite: #Verifica se o valor informado foi maior que o limite, se for a operação falha
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES: #Verifica se a quantidade de saques é maior ou igual ao limite, se for a operação falha 
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0: #Caso nenhuma das condições acima forem satisfeitas, vamos nessa
            saldo -= valor #Retira o valor informado do saldo do cliente 
            extrato += f"Saque: R$ {valor:.2f}\n" #Guarda esse valor dentro da variavel extrato
            numero_saques += 1 #Incrementa uma movimentação na variavel "numero_saques"

        else:
            print("Operação falhou! O valor informado é inválido.") #Se o valor informado for menor que 0 

    elif opcao == 3: #Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) #Caso o valor do extrato esteja em branco (valor seja falso/vazio)
        print(f"\nSaldo: R$ {saldo:.2f}") #Caso não esteja
        print("==========================================")

    elif opcao == 4: #Sair
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")