# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de
# qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
# numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo
# abaixo:

tabuada = int(input("Deixa eu te ajudar com a tabuada <3 : "))

print("Tabuada de",tabuada)
for i in range(1,11):
    print(f"{tabuada} x {i} = {tabuada * i}")