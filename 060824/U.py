# Crie uma exceção personalizada (subclasse de Exception) com uma mensagem específica. Use essa exceção em um contexto relevante.​

class DivisaoPorZeroException(Exception):
    def __init__(self, mensagem="Erro: Divisão por zero não é permitida."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    if numero2 == 0:
        raise DivisaoPorZeroException()
    if numero1 == 0:
        raise DivisaoPorZeroException()
    
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")

except DivisaoPorZeroException as e:
    print(e)
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")
