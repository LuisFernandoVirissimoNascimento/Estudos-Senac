# Sequência de Fibonacci:
# Crie um programa que gera os primeiros ‘n’ números da sequência de Fibonacci. A
# sequência começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fibonacci_sequence
    
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

n = int(input("Digite o número de termos da sequência de Fibonacci que deseja gerar: "))

print("Os primeiros", n, "números da sequência de Fibonacci são:")
print(fibonacci(n))