# 5. Altere o programa anterior permitindo ao usuário informar as
# populações e as taxas de crescimento iniciais. Valide a entrada e permita
# repetir a operação. 

anos = 0
paisA = 80000
paisACrescimento = 1.03

paisB = 200000
paisBCrescimento = 1.015
while True:
    print("Vamos calcular quanto tempo demora para o pais A ultrapassar o pais B")
    paisA = float(input("Qual a população do pais A ?\n"))
    paisACrescimento = float(input("E Qual a taxa de crescimento ?\n"))
    paisACrescimento = (paisACrescimento / 100) + 1

    paisB = float(input("Qual a população do pais B ?\n"))
    paisBCrescimento = float(input("E Qual a taxa de crescimento ?\n"))
    paisBCrescimento = (paisBCrescimento / 100) + 1  
    while True:
        if paisA < paisB :
            anos += 1;
            paisA *= paisACrescimento
        else:
            print(f"Anos necessários para que a pop A passe da Pop B foi {anos} que agora possue uma população de {int(paisA)} ")
            break

    bah = input("Quer continuar ? S/N\n")
    if bah == "N":
        break