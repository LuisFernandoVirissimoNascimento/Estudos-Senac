# 15. Dicionário de Notas:
# Crie um dicionário com nomes de disciplinas e suas notas. 
# Exiba a disciplina com a maior nota.

dicionatie = {"Luis" : 3, "Sérgio" : 500, "Diego" : 69, "Bruna" : 3000000000000000000}

bah = 0

for i in dicionatie:
    if dicionatie[i] > bah:
        bah = dicionatie[i]
print(bah)