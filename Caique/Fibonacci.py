def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Exemplo de uso
n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
print(f"Os primeiros {n} termos são: {fibonacci(n)}")
