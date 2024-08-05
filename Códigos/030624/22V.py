# Cálculo de Média Ponderada:
# Escreva um programa que pede ao usuário para digitar as notas e os pesos de várias
# disciplinas e, em seguida, calcula a média ponderada.

def calcular_media_ponderada():
    num_disciplinas = int(input("Digite o número de disciplinas: "))
    
    notas = []
    pesos = []
    
    # Solicita ao usuário as notas e pesos das disciplinas
    for i in range(num_disciplinas):
        nota = float(input(f"Digite a nota da disciplina {i+1}: "))
        notas.append(nota)
        
        peso = float(input(f"Digite o peso da disciplina {i+1}: "))
        pesos.append(peso)
    
    # Calcula a média ponderada
    soma_notas_ponderadas = 0
    soma_pesos = 0
    for nota, peso in zip(notas, pesos):
        soma_notas_ponderadas += nota * peso
        soma_pesos += peso
    
    media_ponderada = soma_notas_ponderadas / soma_pesos
    
    print("A média ponderada das disciplinas é:", media_ponderada)

# Exemplo de uso da função:
calcular_media_ponderada()
