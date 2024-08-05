# 2. Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem
# de erro e voltando a pedir as informações. 

while True:
    bobon = input("seu login")
    bibin = input("sua senha pls")
    if bobon == bibin:
        print(":(")
    else:
        break