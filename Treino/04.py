# O engenheiro de uma empresa precisa calcular a quantidade de cabos de rede necessários para instalar um laboratório com "n" pontos de redes. O engenheiro sabe que a distância entre cada ponto de rede será de "r" metros (razão) e que o comprimento total dos cabos é igual à soma das distâncias entre todos os pontos de rede.
# Para facilitar o cálculo, o engenheiro decidiu usar uma Progressão Aritmética (PA) para representar as distâncias entre os pontos de rede. Você precisa escrever um programa Python que ajude o engenheiro a calcular a quantidade de cabos de rede necessários. Seu programa deve:
# Solicitar ao usuário os dados de entrada da PA que é dado por: a + (n-1)*r, onde "a" é o primeiro termo, "n" é o número de termos e "r" é a razão da progressão.
# Calcular total dos cabos de rede necessário, que é igual à soma dos termos de todos os pontos de rede. Exibir na tela a quantidade de cabos de rede necessários para instalar o laboratório.
# Exibir também quarto termo e o termo central da progressão aritmética.
# Para calcular o termo central o programa deve somar o 1º e ultimo termo da Progressão Aritmética e dividir por 2.
# Por fim, o programa deve retornar uma lista com os termos da PA e ser testado com diferentes valores de "n" e "r" para garantir que ele esteja funcionando corretamente e produzindo resultados precisos.
# Entrada


# >>Digite o primeiro termo da PA: 2
# >>Digite a razão: 1.5
# >>Digite a quantidade de termos: 7
 
 #a + (n-1)*r, onde "a" é o primeiro termo, "n" é o número de termos e "r" é a razão da progressão.
# Saída


# >> [2.0, 3.5, 5.0, 6.5, 8.0, 9.5, 11.0]
# >> O quinto termo é: 8.0
# >> O termo central é: 6.5
# >> Soma dos termos: 45.5
 
# Entrada


# >>Digite o primeiro termo da PA: 3
# >>Digite a razão: 2.5
# >>Digite a quantidade de termos: 7
 
 
# Saída


# >> [3.0, 5.5, 8.0, 10.5, 13.0, 15.5, 18.0]
# >> O quinto termo é: 13.0
# >> O termo central é: 10.5
# >> Soma dos termos: 73.5
# Obs. Não é permitido a utilização bibliotecas
# Obs. Utilizar tratamento de exceção

a = 2
r = 1.5
n = 7
print( a + (1-1)*r)
print( a + (n-1)*r)

listTermosPA = []
quintoTermo = 0

# For loop of amount of termos, start with 1. append the thing

while True:
    while True:
                try:
                    a = int(input("Digite o primeiro Termo: "))
                    break
                except:
                    print("Valor inválido. Por favor inserir um valor válido\n")
    while True:
                try:
                    r = float(input("Digite o a razão: "))
                    break
                except:
                    print("Valor inválido. Por favor inserir um valor válido\n")
    while True:
                try:
                    n = int(input("Digite a quantia de termos: "))
                    break
                except:
                    print("Valor inválido. Por favor inserir um valor válido\n")
    break
for i in range(n):
    i += 1
    if i == 5:
        result = a + (i-1)*r
        quintoTermo = result
    else:
        result = a + (i-1)*r

    print(result)
    listTermosPA.append(result)

print(listTermosPA)
print(f"O Quinto termo é {quintoTermo}")
quantiaLista = len(listTermosPA)
print(f"O Termo central é {listTermosPA[int(quantiaLista / 2)]}")
soma = 0
for i in listTermosPA:
    soma += i
print(f"A Soma dos termos é {soma}")