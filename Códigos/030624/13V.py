# Verificação de Palíndromo:
# Faça um programa que verifica se uma palavra ou frase é um palíndromo. Um palíndromo é
# uma palavra ou frase que se lê da mesma forma de trás para frente. Por exemplo, “arara” é um palíndromo.

def verificar_palindromo(texto):
    # Remover espaços em branco e converter para minúsculas
    texto = texto.replace(" ", "").lower()
    # Verificar se o texto é igual ao seu inverso
    return texto == texto[::-1]

# Exemplo de uso
palavra = input("Digite uma palavra ou frase: ")
if verificar_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")