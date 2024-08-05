#Escreva um programa que faça um cadastro de clientes. Seu programa deve:
# [Entrada]: receber os seguintes dados do usuário:
# 1) o nome completo; 2) o RG do cliente; 3) o CPF e; 4) o telefone do cliente.
# [Processamento]: Seu programa deve armazenar todos os dados em uma ÚNICA LISTA. [Saída]: AO FINAL, SOMENTE AO FINAL, Seu programa deve mostrar (um cliente por linha):
# a) o nome completo do paciente, b) O RG; c) o CPF e; d) o telefone do cliente.
# Obs: o usuário deve fazer esse procedimento para quantos clientes ELE QUISER.
# Exemplo de Entrada:
# Digite o nome completo do cliente (ou digite 'sair' para encerrar): Enilda Caceres
# Digite o RG do cliente: 5478
# Digite o CPF do cliente: 5588
# Digite o telefone do cliente: 5877
# Digite o nome completo do cliente (ou digite 'sair' para encerrar): sair
# Exemplo de Saída:
# Cadastro de Clientes:
# ====================
# Nome: Enilda Caceres, RG: 5478, CPF: 5588, Telefone: 5877


nomeCliente = ""
rgCliente = ""
cpfCliente = 0
telefoneCliente = 0
newClientInt = 0
listaCliente = []
while True:
    confirm = input("1 - Registrar Cliente\n2 - Sair\n")
    if confirm == "1":
        while True:
            nomeCliente = input("Digite o nome completo do cliente (ou digite 'sair' para encerrar): ")
            if nomeCliente == "sair":
                break
            rgCliente = input("Digite o RG do cliente: ")
            while True:
                try:
                    cpfCliente = int(input("Digite o CPF do cliente: "))
                    break
                except:
                    print("Valor inválido. Por favor inserir um valor válido\n")
            while True:
                try:
                    telefoneClienteCliente = int(input("Digite o Telefone do cliente: "))
                    break
                except:
                    print("Valor inválido. Por favor inserir um valor válido\n")
            listaCliente.append(nomeCliente)
            listaCliente.append(rgCliente)
            listaCliente.append(telefoneCliente)
            listaCliente.append(cpfCliente)
            break
    elif confirm == "2":
        break
    else:
        print("Valor Inválido")

print("Cadastro de Clientes:\n\n====================")
for i in range(len(listaCliente)):
    # We take every four I because that is a new client.
    i += 1
    if i - newClientInt == 1:
        print("\nNome:" , listaCliente[i - 1] ,end = "")
    if i - newClientInt == 2:
        print(", RG:" ,listaCliente[i - 1] ,end = "")
    if i - newClientInt == 3:
        print(", CPF:" , listaCliente[i - 1],end = "")
    if i - newClientInt == 4:
        print(", Telefone:" , listaCliente[i - 1],end = "")
    if i % 4 == 0:
        # Means it's the end ?
        newClientInt += 4