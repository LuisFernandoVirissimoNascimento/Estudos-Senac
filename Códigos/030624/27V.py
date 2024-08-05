# Verificação de Anagramas:
# Faça um programa que verifica se duas palavras são anagramas (ou seja, possuem as
# mesmas letras, mas em ordem diferente).

def sao_anagramas(palavra1, palavra2):
    # Converte as palavras para letras minúsculas e remove espaços em branco
    palavra1 = palavra1.lower().replace(" ", "")
    palavra2 = palavra2.lower().replace(" ", "")
    
    # Verifica se as duas palavras têm o mesmo conjunto de letras
    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False

# Exemplo de uso da função:
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sao_anagramas(palavra1, palavra2):
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")
