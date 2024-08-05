# Número Invertido:
# Crie um software que recebe um número do usuário, passa esse valor para uma função e ela
# retorna o número escrito ao inverso. Por exemplo, se o usuário der o valor 1234, a função
# deve retornar 4321. Dica: primeiro, crie uma função que conta quantos dígitos tem um número.

def more(inpute):
    for char in inpute[::-1]:
        print(char,end="")

more("1234")