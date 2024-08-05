# Cálculo de Juros Compostos:
# Faça um programa que calcula o montante final de um investimento com juros compostos.
# O usuário deve fornecer o capital inicial, a taxa de juros anual e o período de investimento em anos.

def calcular_juros_compostos(capital, taxa, periodo):
    montante = capital * (1 + taxa/100)**periodo
    return montante

capital_inicial = float(input("Digite o capital inicial: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (%): "))
periodo_anos = int(input("Digite o período de investimento em anos: "))

montante_final = calcular_juros_compostos(capital_inicial, taxa_juros_anual, periodo_anos)

print("O montante final do investimento é:", montante_final)