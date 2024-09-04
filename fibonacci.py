#Questão 1 
def is_fibonacci(n):
    
    def e_quadrado_perfeito(x):
        s = int(x ** 0.5)
        return s * s == x

    
    return e_quadrado_perfeito(5 * n * n + 4) or e_quadrado_perfeito (5 * n * n - 4)


numero = int(input("Informe um número: "))

# Verificando se o número pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#Questão 2
def verificar_letra_a(string):
    
    count_a = string.count('a')
    count_A = string.count('A')
    
    
    total_count = count_a + count_A
    
    
    if total_count > 0:
        print(f"A letra 'a' ocorre {total_count} vez(es) na string.")
    else:
        print("A letra 'a' não ocorre na string.")


string = input("Informe uma string: ")


verificar_letra_a(string)



