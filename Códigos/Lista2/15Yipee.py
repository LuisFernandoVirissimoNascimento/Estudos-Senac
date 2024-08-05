# 16. A série de Fibonacci é formada pela sequência
# 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
# n−ésimo termo.

intie = int(input("Dite um número: "))
sequênciaFibonacci = [0, 1]

while sequênciaFibonacci[-1] + sequênciaFibonacci[-2] <= intie:
    sequênciaFibonacci.append(sequênciaFibonacci[-1] + sequênciaFibonacci[-2])

print(sequênciaFibonacci)