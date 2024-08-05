# 17. A série de Fibonacci é formada pela sequência
# 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
# valor seja maior que 500. 

intie = 700
sequênciaFibonacci = [0, 1]

while sequênciaFibonacci[-1] + sequênciaFibonacci[-2] <= intie:
    sequênciaFibonacci.append(sequênciaFibonacci[-1] + sequênciaFibonacci[-2])

print(sequênciaFibonacci)