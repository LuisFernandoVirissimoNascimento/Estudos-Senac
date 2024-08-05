# 18. Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 

intie = int(input("Dite um número: "))
intia = intie
for i in range(intie -1, 0, -1):
    intia *= i
    
print(intia)