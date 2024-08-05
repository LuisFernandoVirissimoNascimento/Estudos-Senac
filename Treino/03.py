print("Jogo de quiz !!!!!!!!")
pontos = 0
answer1 = input("Qual a capital do brasil ?\nSua resposta : ")
if answer1 != "Brasilia":
    print("Resposta Incorreta")
else:
    pontos += 1
    print(f"Resposta Correta !\nVocê fez {pontos} pontos.")


answer1 = input("Quem escreveu Dom Quixote ?\nSua resposta : ")
if answer1 != "Miguel de Cervantes":
    print("Resposta Incorreta")
else:
    pontos += 1
    print(f"Resposta Correta !\nVocê fez {pontos} pontos.")


answer1 = input("Quanto é 2 + 2 ?\nSua resposta : ")
if answer1 != "4":
    print("Resposta Incorreta")
else:
    pontos += 1
    print(f"Resposta Correta !\nVocê fez {pontos} pontos.")