
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        print(f'O número {n} pertence a sequência de Fibonacci')
    else:
        print(f'O número {n} não pertence a sequência de Fibonacci')

fibonacci(13)