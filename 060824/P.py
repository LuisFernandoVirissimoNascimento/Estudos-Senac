# Crie uma classe que aceite a digitação de dois números e realize a divisão entre eles, exibindo o resultado.​

# Trate as seguintes exceções:​

# ArithmeticException quando ocorrer uma divisão por zero.​

# InputMismatchException  quando o valor informado não for numérico​


try:
    numero1 = float(input("[red]Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")
