# 2. Média de Notas:
# Crie um dicionário com nomes de alunos e suas notas. Calcule a média das notas e exiba o resultado
notasAlunos = {'Babito' : 3, 'eheheheheh' : 10, '6':5}
bonbador = 0
bebedor = 0
for i in notasAlunos:
    bonbador += 1
    bebedor += notasAlunos[i]

print(f"A Média dos alunos é {bebedor / bonbador}")
