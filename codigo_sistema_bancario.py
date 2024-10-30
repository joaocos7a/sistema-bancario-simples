# PRIMEIRA VERSÃO

menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Deposite o valor desejado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        
        else:
            print("Valor informado inválido")

    elif opcao == "S":
        valor = float(input("Informe o valor de saque desejado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente, tente outro valor!")

        elif excedeu_limite:
            print("Valor solicitado maior que o limite diário, tente outro valor!")

        elif excedeu_saques:
            print("Limite de saque diário atingido, tente novamente amanhã!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida!")
    
    elif opcao == "E":
        print("\n=============== EXTRATO ===============")
        print("Não houve movimentação" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("========================================")

    elif opcao == "Q":
        break
    print("Obrigado por ser nosso cliente!")

else:
    print("Operação inválida, retorne ao menu e selecione a opção desejada")