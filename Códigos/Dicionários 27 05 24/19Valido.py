# 19. Dicionário de Temperaturas:
# Crie um dicionário com nomes de cidades e suas temperaturas máximas. Exiba a
# cidade com a temperatura mais alta.

dicionatie = {"THE SUN" : 3, "Antartica" : -500, "Campo Grande" : 69, "That cute af girl you see on the elevator from time to time" : 3000000000000000000}

bah = 0

for i in dicionatie:
    if dicionatie[i] > bah:
        bah = dicionatie[i]
print(bah)