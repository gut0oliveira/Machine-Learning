menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo+=valor
            extrato += f"Depósito R$ {valor:.2f}\n"

        else:
            print("Operação falhou: o valor informado é inválido.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou: você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou: você não tem limite suficiente.")

        elif excedeu_saques:
            print("Operação falhou: número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato =+ f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "E":
        print("#"*25)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("#"*25)

    elif opcao == "Q":
        print("Você saiu do sistema!")
        break

    else:
        print("Opção inválida, por favor selecione novamento a operação desejada.")


