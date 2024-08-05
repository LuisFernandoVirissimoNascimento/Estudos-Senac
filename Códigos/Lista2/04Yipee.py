# 4. Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que a população
# de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça
# um programa que calcule e escreva o número de anos necessários para
# que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento. 
anos = 0
paisA = 80000
paisACrescimento = 1.03

paisB = 200000
paisBCrescimento = 1.015
while True:
    if paisA < paisB :
        anos += 1;
        paisA *= paisACrescimento
    else:
        print(f"Anos necessários para que a pop A passe da Pop B foi {anos} que agora possue uma população de {int(paisA)} ")
        break