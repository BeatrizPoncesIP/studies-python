produto_1 = 20
produto_2 = 10

print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

##########################################
print()  # adiciona uma quebra de linha


frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas)
print("limao" in frutas)
print("Python" in curso)

##########################################
print()  # adiciona uma quebra de linha


saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

##########################################
print()  # adiciona uma quebra de linha


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)