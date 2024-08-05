notas = [float(input("Me dê a nota do aluno : ")) for i in range(3)]
# 4 é a harmonização
floatie1 = 1 / (notas[0] + 4)
floatie2 = 1 / (notas[1] + 4)
floatie3 = 1 / (notas[2] + 4)

notaMédia = (3 / ((floatie1) + (floatie2) + (floatie3))) - 4

if (notaMédia >=5):
    print(f"O aluno foi aprovado com média {notaMédia}")  

else:
    print(f"O aluno foi reprovado com média {notaMédia}")