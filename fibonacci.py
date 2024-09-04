def is_fibonacci(n):
    # Função para verificar se um número é quadrado perfeito
    def e_quadrado_perfeito(x):
        s = int(x ** 0.5)
        return s * s == x

    # um ou ambos de (5*n^2 + 4) ou (5*n^2 - 4) forem quadrados perfeitos.
    return e_quadrado_perfeito(5 * n * n + 4) or e_quadrado_perfeito (5 * n * n - 4)

# Número que queremos verificar
numero = int(input("Informe um número: "))

# Verificando se o número pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
