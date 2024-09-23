def Fibonacci(n):
    x, z = 0, 1
    while x < n:
        x, z = z, x + z
    return x == n

#numero = int(input("Informe um número: "))
# Utilizando um numero como exemplo
numero = 5
if Fibonacci(numero):
    print(f"O numero {numero} pertence a sequencia")
else:
    print(f"O numero {numero} nao pertence a sequencia.")