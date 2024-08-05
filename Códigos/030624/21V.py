# Conversão de Bases Numéricas:
# Crie um programa que converte um número decimal para binário, octal ou hexadecimal,
# conforme a escolha do usuário.


def conversao_bases():
    numero_decimal = int(input("Digite o número decimal a ser convertido: "))
    print("Escolha a base para conversão:")
    print("1. Binário")
    print("2. Octal")
    print("3. Hexadecimal")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        print("O número em binário é:", bin(numero_decimal))
    elif opcao == 2:
        print("O número em octal é:", oct(numero_decimal))
    elif opcao == 3:
        print("O número em hexadecimal é:", hex(numero_decimal))
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Exemplo de uso da função:
conversao_bases()
