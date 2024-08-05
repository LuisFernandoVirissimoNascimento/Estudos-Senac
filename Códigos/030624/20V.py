# Validação de CPF:
# Implemente um programa que verifica se um número de CPF é válido. O CPF é composto
# por 11 dígitos e possui um algoritmo de validação específico.

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remove pontos e traços do CPF
    if len(cpf) != 11 or not cpf.isdigit():  # Verifica se o CPF possui 11 dígitos numéricos
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto

    # Verifica o primeiro dígito verificador
    if digito_verif_1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto

    # Verifica o segundo dígito verificador
    if digito_verif_2 != int(cpf[10]):
        return False

    return True

cpf = input("Digite o número do CPF (apenas números): ")

if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
