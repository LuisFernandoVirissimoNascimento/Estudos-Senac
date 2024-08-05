# 28. Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 
bah = 0.0
bih = 0.0
while True:
    intie = float(input("Qual o tamanho da turma nova, abaixo de 40, digite 0 se quiser acabar.\n "))
    if intie == 0:
        break
    elif intie >= 1 and intie <= 40:
        bih += 1
        bah += intie

bah /= bih
print(f"A Média de alunos é {int(bah)}")