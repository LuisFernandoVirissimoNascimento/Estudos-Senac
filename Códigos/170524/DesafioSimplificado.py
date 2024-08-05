isEmployeeWhile = False
isLeaving = False
isEmployee = input("Você é um funcionário ?\n")
if isEmployee == "sim":
    isEmployeeWhile = True
    employeeCode = input("Qual a sua matricula ?\n")
    name = input("Qual o seu nome ?\n")
    birthdate = input("Qual sua data de nascimento em formato xx/xx/xxxx\n")
    cpfNum = input("Qual seu cpf ?\n")
else:
    name = input("Qual seu nome ?\n")
    cpfNum = input("Qual seu cpf ?\n")

print("""
Seção 13 - Alimentos : Carne de pato (138) / Pato de Carne (128)
Seção 18 - Cosplay : Chapéu de palha (1038) / Flecha de Stand (7)
Seção 69 - Patos de Borracha : Pato de borracha daora com Capacete e corrente de ouro (6969) / Pato de borracha não muito legal (6000)
""")

sec13Names = ["Carne de pato","Pato de Carne"]
sec13Codes = ["138","128"]
sec13Prices = [10,10]

sec18Names = ["Chapéu de palha","Flecha de stand"]
sec18Codes = ["1038","7"]
sec18Prices = [10,10]

sec69Names = ["Pato de borracha daora com capacete e corrente de ouro","Pato de borracha não muito legal"]
sec69Codes = ["6969","6000"]
sec69Prices = [10,10]

listNamesClientHas = []
listCodesClientHas = []
listPricesClientHas = []


# Parte separada só para o funcionário para não editar código ç.ç

employeeItemNames = ["Cocaina","Faca AK-47","Crack","Carne de Pato","Pato de Carne"]
employeeItemTypes = ["Ilegal","Combate","Ilegal","Alimentos","Alimentos"]
employeeItemSubTypes = ["Droga","Arma","Droga","Carne","Carne"]
employeeItemPrices = [300,1000000000,1,10,10]
employeeItemCodes = [77,3,78,138,128]

while True:
    if isEmployeeWhile: # Área do funcionário.
        if isLeaving:
            break
        while True:
            funçãoSelecionada = input("Qual função você quer ?\n0 - Sair\n1 - Visualizar Estoque\n2 - Remover produto do estoque\n3 - Adicionar produto ao estoque\n4 - Atualizar preço do estoque\n")
            if funçãoSelecionada == "0": # Leave
                isLeaving = True
                break
            elif funçãoSelecionada == "1": # See Stock
                for i in range(len(employeeItemNames)):
                    print("\nNome do produto :",employeeItemNames[i],"\nTipo :",employeeItemTypes[i],"\nSubtipo :",employeeItemSubTypes[i],"\nPreço : R$",employeeItemPrices[i],"\nCódigo :",employeeItemCodes[i])
            elif funçãoSelecionada == "2": # Remove from stock
                itemToBeRemoved = int(input("Qual o código do produto a ser removido ?\n"))
                for i in range(len(employeeItemCodes)):
                    if employeeItemCodes[i] == itemToBeRemoved:
                        employeeItemNames.remove(employeeItemNames[i])
                        employeeItemTypes.remove(employeeItemTypes[i])
                        employeeItemSubTypes.remove(employeeItemSubTypes[i])
                        employeeItemPrices.remove(employeeItemPrices[i])
            elif funçãoSelecionada == "3": # Add to stock
                print("Tenha certeza da inserção para não causar erro ao banco de dados.")
                employeeItemNames.append(input("Qual o nome do produto a ser inserido\n"))
                employeeItemTypes.append(input("Qual o tipo do produto a ser inserido\n"))
                employeeItemSubTypes.append(input("Qual o subtipo do produto a ser inserido\n"))
                employeeItemPrices.append(float(input("Qual o preço do produto a ser inserido\n")))
                employeeItemCodes.append(int(input("Qual o código do produto a ser inserido\n")))
            elif funçãoSelecionada == "4": # Update price
                itemToUpdatePrice = int(input("Qual o código do produto a ter seu preço atualizado ?\n"))
                for i in range(len(employeeItemCodes)):
                    if employeeItemCodes[i] == itemToUpdatePrice:
                        employeeItemPrices[i] = float(input("Qual o novo preço ?\n"))
            else:
                print("Função inválida")
    else:
        if isLeaving:
            break
        while True:
            funçãoSelecionada = input("Qual função você quer ?\n0 - Sair\n1 - Adicionar produto ao carrinho\n2 - Remover produto\n3 - Visualizar carrinho\n4 - Finalizar Comprar\n")
            if funçãoSelecionada == "0": # Keave
                isLeaving = True
                break
            elif funçãoSelecionada == "1":
                # add shit
                whichSection = input("Qual tipo de produto você quer adicionar ao carrinho, digite o código de seção do tipo de produto que quer :)\n")
                if whichSection == "13":
                    whichProduct = input("Qual o produto que você quer dessa seção ?\n")
                    if whichProduct == "138":
                        listNamesClientHas.append(sec13Names[0])
                        listCodesClientHas.append(sec13Codes[0])
                        listPricesClientHas.append(sec13Prices[0])
                    elif whichProduct == "128":
                        listNamesClientHas.append(sec13Names[1])
                        listCodesClientHas.append(sec13Codes[1])
                        listPricesClientHas.append(sec13Prices[1])
                    else:
                        print("Produto Inválido")
                elif whichSection == "18":
                    whichProduct = input("Qual o produto que você quer dessa seção ?\n")
                    if whichProduct == "1038":
                        listNamesClientHas.append(sec18Names[0])
                        listCodesClientHas.append(sec18Codes[0])
                        listPricesClientHas.append(sec18Prices[0])
                    elif whichProduct == "7":
                        listNamesClientHas.append(sec18Names[1])
                        listCodesClientHas.append(sec18Codes[1])
                        listPricesClientHas.append(sec18Prices[1])
                    else:
                        print("Produto Inválido")
                elif whichSection == "69":
                    whichProduct = input("Qual o produto que você quer dessa seção ?\n")
                    if whichProduct == "6969":
                        listNamesClientHas.append(sec69Names[0])
                        listCodesClientHas.append(sec69Codes[0])
                        listPricesClientHas.append(sec69Prices[0])
                    elif whichProduct == "6000":
                        listNamesClientHas.append(sec69Names[1])
                        listCodesClientHas.append(sec69Codes[1])
                        listPricesClientHas.append(sec69Prices[1])
                    else:
                        print("Produto Inválido")
                else:
                    print("Seção Inválida.")        
            elif funçãoSelecionada == "2":
                # break thoguh it all
                if len(listNamesClientHas) == 0:
                    print("Não tem produto no carrinho.")
                else:            
                    for i in range(len(listNamesClientHas)):
                        print("Nome do Produto :",listNamesClientHas[i],"\nPreço : R$",listPricesClientHas[i],"\nPosição dele :",i)
                    whichProductToRemove = int(input("Qual dos produtos no seu carrinho você quer que seja retirado ? Digite a posição dele.\n"))
                    listNamesClientHas.remove(listNamesClientHas[whichProductToRemove])
                    listCodesClientHas.remove(listCodesClientHas[whichProductToRemove])
                    listPricesClientHas.remove(listPricesClientHas[whichProductToRemove])
            elif funçãoSelecionada == "3":
                # break thoguh it all
                print("No Carrinho :\n")
                for i in range(len(listNamesClientHas)):
                    print("Nome do Produto :",listNamesClientHas[i],"\nPreço : R$",listPricesClientHas[i])
            elif funçãoSelecionada == "4":
                # break thoguh it all
                print("No Carrinho :\n")
                preçoTotal = 0
                for i in range(len(listNamesClientHas)):
                    print("Nome do Produto :",listNamesClientHas[i],"\nPreço : R$",listPricesClientHas[i])
                    preçoTotal += listPricesClientHas[i]
                print("Preço total sem imposto : R$",preçoTotal)        
                # Taxes
                taxesCalc = preçoTotal * 1.05
                taxesCalc = taxesCalc * 1.08
                taxesCalc = taxesCalc * 1.12
                taxado = taxesCalc - preçoTotal
                print("Preço do imposto : R$",taxado)
                preçoTotal = taxesCalc
                print("Preço total : R$",preçoTotal)
                proceedWithPurchase = input("Gostaria de prosseguir com a compra ?\n")
                if proceedWithPurchase == "sim":
                    while True:
                        whichPaymentMethod = input("Qual tipo de pagamento vai ser usado ?\nDinheiro, Pix, Crédito, Débito ou Voucher ?\n")
                        if whichPaymentMethod == "Dinheiro":                    
                            quantiaididiaiefistbump = float(input("Quantos reais vai pagar ?\n"))
                            if quantiaididiaiefistbump == preçoTotal:
                                print("Pago em dinheiro")
                                break
                            elif quantiaididiaiefistbump > preçoTotal:
                                troctrocotroco = quantiaididiaiefistbump - preçoTotal
                                print("Seu troco é R$",troctrocotroco)
                                break
                            else:
                                print("Quantia insuficiente, use outro método de pagamento.")
                        elif whichPaymentMethod == "Pix":
                            print("Pago em pix.")
                            break
                        elif whichPaymentMethod == "Crédito":
                            print("Pago em crédito")
                        elif whichPaymentMethod == "Débito":
                            print("Pago em débito")
                        elif whichPaymentMethod == "Voucher":
                            print("Pago em voucher.")
                else:
                    pass
            else:
                # Nu uh
                print("Função Inválida")        