conta_normal = False
conta_universitaria = True
conta_especial = False
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:



    ##################################################

    status = "Sucesso" if saldo >= saque else "Falha"
    print(f"{status} ao realizar o saque!")

    ##################################################



elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")