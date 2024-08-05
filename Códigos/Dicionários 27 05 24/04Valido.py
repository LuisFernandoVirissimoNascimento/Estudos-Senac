# 4. Tradutor Simples:
# Crie um dicionário com algumas palavras em inglês e suas traduções em português. 
# Peça ao usuário para digitar uma palavra em inglês e exiba a tradução correspondente.

dicionatie = {"Banana" : "Banana", "1" : "1", "Explosion" : "Explosão", "War and glory" : "Guerra e glória"}

print(dicionatie.keys())
tradução = input("Qual dessas palavras você quer a tradução ?\n")
if tradução in dicionatie:
    print(dicionatie[tradução])
