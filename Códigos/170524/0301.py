# uma empresa de RH precisa automatizar as tarefas de processo seletivo devido a alta demanda de seus clientes por novos funcionários.

# Você foi contratado para desenvolver o sistema de inscrição dos canditados para as vagas e o programa deve validar se: 

# 1 - se a pessoa possue tem no minimo 18 anos, ela passa na primeira fase do processo seletivo.

# 2 - Se ela possui curso de qualificação na área ela passa da segunda fase do processo seletivo.

# 3 - Na terceira fase a pessoa realiza uma prova de conhecimentos especificos, se a nota for maior que 7, está ápita para etapa final.

# Se não recebe um email com mensagem de agradecimento.

# seu programa deve conter as seguintes variáveis :

cargo = ""
nome_completo = ""
idade = 0
email = ""
curso = ""
nota = 0
mensagem = "" # Honestamente tem no código mas não é usado.

mensagemAprovação = "Você passou para a próxima fase !"
mensagemErro = "Obrigado por sua participação."

# Você deve analisar os requisitos do sistema, elaborar um fluxograma do processo seletivo e codificar sua solução.
# Obs, a cada fase a pessoa recebe o seguinte email: Parabéns, você passou para a próxima fase ou Obrigado por sua participação.

#### No Validation

while True:
    cargo = input("Qual cargo você quer se inscrever para ?\n")
    nome_completo = input("Qual seu nome completo ?\n")
    email = input("Qual seu email ?\n")
    print(mensagem)

    idade = int(input("Quantos anos você possue ?\n"))
    if idade < 18:
        print(mensagemErro)
        break
    else:
        print(mensagemAprovação)
    
    curso = input("Possue qualificação na área ? Sim ou não\n")
    if curso.lower() == "sim":
        print(mensagemAprovação)
    else:
        print(mensagemErro)
        break

    nota = float(input("Qual nota você tirou na prova ?\n"))
    if nota > 7:
        print(mensagemAprovação)
        break
    else:
        print(mensagemErro)
        break



    