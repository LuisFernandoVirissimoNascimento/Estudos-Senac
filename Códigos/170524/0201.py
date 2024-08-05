# so we gon have like 3 movies or smth like that and then we gon like get paid and such idk man
# Crie um código que receba o nome da pessoa, receba o valor do ingresso e o tipo do ingresso (meia ou inteira), caso seja meia receba a carteirinha.
# calcule no final o valor total da compra com todos os ingressos comprados e imprima quais os tipos de ingresso.

# codigo de uso da carteirinha é lenght 9

# Primeiro vamos saber quais são os filmes e seus preços.

filmes = ["1 - Zoolander","2 - Harry potter e a pedra filosofal","3 - O Senhor dos Anéis: A Irmandade do anel"]
preços = [5.0,10.0,15.0]

nome = ""
ticketsCompradosNomeDoCliente = []
ticketsCompradosNomeDoFilme = []
ticketsCompradosPreçoDoFilme = []
ticketsCompradosCarteirinha = []
preçoAtual = 0
filmeAtual = ""
compraTotal = 0
while True:
    while True:
        try:
            while True:
                funçãoRequisitada = int(input("Funções disponíveis : \n0 - Sair \n1 - Comprar ticket \n2 - Mudar Nome \n3 - Visualizar Tickets a comprar\nInsira o número da função requisitada : "))
                if funçãoRequisitada < 0 or funçãoRequisitada > 3:
                    print("\nPor favor, insira um número válido.\n")
                else:
                    break
            break
        except KeyboardInterrupt:
                print("\n\nSaindo do código")
                funçãoRequisitada = 0
                break   
        except:
            print("\nPor favor, insira um número válido.\n")
    match funçãoRequisitada:
        case 0: # Saida do sistema
            print("\nSaindo do sistema\n")
            break
        case 1: # Compra do ticket
            # Se o nome estiver vazio solicite um novo nome, se a pessoa quiser mudar o nome dê a opção para mudar aqui também.
            # Após isso mostre os filmes a serem comprados e seus preços.
            # Solicite qual filme a pessoa quer e se ela está usando carteirinha. Se estiver usando carteirinha corte o preço ao meio antes de adicionar a compra total.
            if nome == "":
                nome = input("Insira seu nome :\n")
            print("Filmes disponíveis para compra :\n")
            for i in range(3):
                print(f"Filme : {filmes[i]}, Preço : R$ {preços[i]}")
            # Ordináriamente eu teria botões para o cara selecionar, mas ja que estamos programando em data teremos que solicitar input de numero >:(
            while True:
                try:
                    while True:
                        filmeRequisitado = int(input("Qual filme gostaria de comprar um ticket para ? Insira o número do filme :\n "))
                        if filmeRequisitado < 0 or filmeRequisitado > 3:
                            print("\nPor favor, insira um número válido.\n")
                        else:
                            # Pegue o preço.
                            i = filmeRequisitado - 1
                            filmeAtual = filmes[i]
                            preçoAtual = preços[i]
                            break
                    break
                except KeyboardInterrupt:
                        print("\n\nSaindo do código")
                        funçãoRequisitada = 0
                        break   
                except:
                    print("\nPor favor, insira um número válido.\n")
            while True:
                try:
                    while True:
                        usaCarteirinha = input("Qual tipo de ingresso, inteiro ou meia ?:\n ")
                        if usaCarteirinha.lower() == "inteiro":
                            print("Ticket Inteiro")
                            carteirinhaAtual = "Sem Carteirinha"
                            # Preço atual continua normal
                            break
                        elif usaCarteirinha.lower() == "meia":
                            while True:
                                try:
                                    while True:
                                        númeroDaCarteirinha = int(input("Qual o número de uso da carteirinha ? Deve possuir 9 digitos. :\n "))
                                        if númeroDaCarteirinha == 0:
                                            break
                                        if len(str(númeroDaCarteirinha)) != 9:
                                            print("Número de digitos deve ser igual a 9. Caso não lembre o número, insira 0")
                                        else:
                                            print("huh")
                                            preçoAtual /= 2                    
                                            carteirinhaAtual = "Com Carteirinha"
                                            break
                                        # Possue carteirinha, diminua o preço pela metade
                                    break
                                except KeyboardInterrupt:
                                        print("\n\nSaindo do código")
                                        funçãoRequisitada = 0
                                        break   
                                except:
                                    print("\nPor favor, insira um número válido.\n")
                            break
                        else:
                            print("Insira inteiro ou meia.")
                    break
                except KeyboardInterrupt:
                        print("\n\nSaindo do código")
                        funçãoRequisitada = 0
                        break   
                except:
                    print("\nPor favor, insira um valor válido.\n")
            print("huh")# Agora que você tem o nome do kra, o filme que ele quer e o preço do ticket, insira tudo nas listas.
            print(f"{nome}, o filme que você socilitou é {filmeAtual}, o preço ficou : {preçoAtual}. Deseja adicionar a sua caixa de compras ?\n")
            comprou = input("Sim ou não\n")
            if comprou == "sim":
                # adicione
                ticketsCompradosNomeDoCliente.append(nome)
                ticketsCompradosNomeDoFilme.append(filmeAtual)
                ticketsCompradosPreçoDoFilme.append(preçoAtual)
                ticketsCompradosCarteirinha.append(carteirinhaAtual)
                print("Ticket Adicionado\n")
            else:
                # não adiciona f####e se digitou errado. cansado de validar. to rebelde.
                print("Ticket não adicionado\n")
        case 2: # Mudar nome
            nome = input("Qual nome deseja usar para as compras ?\n")
        case 3:
            if len(ticketsCompradosNomeDoCliente) < 1:
                print("\nNenhum ticket sendo comprado ainda.\n")
            for i in range(len(ticketsCompradosNomeDoCliente)):
                print(f"{ticketsCompradosNomeDoFilme[i]} a ser comprado por {ticketsCompradosNomeDoCliente[i]}, Preço : R${ticketsCompradosPreçoDoFilme[i]} e {ticketsCompradosCarteirinha[i]}")
        case _:
            print("quase la")  

