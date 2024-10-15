def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

# Exemplo de uso
escolha = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para Fahrenheit para Celsius: ").upper()
if escolha == 'C':
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"{celsius}°C em Fahrenheit é {celsius_para_fahrenheit(celsius)}°F")
elif escolha == 'F':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{fahrenheit}°F em Celsius é {fahrenheit_para_celsius(fahrenheit)}°C")
else:
    print("Opção inválida.")
