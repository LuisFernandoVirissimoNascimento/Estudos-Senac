# 24. Faça um programa que mostre todos os primos entre 1 e N sendo N
# um número inteiro fornecido pelo usuário. O programa deverá mostrar
# também o número de divisões que ele executou para encontrar os números
# primos. Serão avaliados o funcionamento, o estilo e o número de testes
# (divisões) executados. 

intie = int(input("Digite um número inteiro maior que 1: "))
total = 0

if intie <= 1:
    print("Número inválido. Por favor, insira um número inteiro maior que 1.")
else:
    print("Números primos entre 1 e", intie, ":")
    for num in range(2, intie+1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            total += 1
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)

print("Número total de divisões realizadas:", total)
