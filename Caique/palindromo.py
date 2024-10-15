def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

# Exemplo de uso
palavra = input("Digite uma palavra ou frase: ")
if eh_palindromo(palavra):
    print(f"'{palavra}' é um palíndromo!")
else:
    print(f"'{palavra}' não é um palíndromo.")
