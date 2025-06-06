def menu():
    print("\n=== Sistema Bancário ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("0 - Sair")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\u2705 Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor <= 0:
        print("❌ Valor inválido para saque.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print(f"❌ Limite máximo por saque é R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print("❌ Número máximo de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque:    - R$ {valor:.2f}\n"
        numero_saques += 1
        print("\u2705 Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

def ver_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")

# Variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
        )

    elif opcao == "3":
        ver_extrato(saldo, extrato)

    elif opcao == "0":
        print("🏦 Obrigado por utilizar o sistema bancário. Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")